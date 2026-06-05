import ctypes

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor

from ..platform.live_client import LiveClient
from ..platform.user import User
from ..data.live_client_config_monitor import LiveClientConfigMonitor
from .overlay_geometry import (
    ABILITY_BOUNDS,
    SUMMONER_SPELL_BOUNDS,
    RECALL_BOUNDS,
    TRINKET_BOUNDS,
    HEALTH_BOUNDS,
    RESOURCE_BOUNDS,
    compute_element_rect,
    compute_minimap_rect,
)

# Win32 extended window style flag for click-through
WS_EX_TRANSPARENT = 0x00000020
WS_EX_LAYERED = 0x00080000
GWL_EXSTYLE = -20


class _OverlayBox(QWidget):
    """A single colored overlay rectangle drawn on top of the game."""

    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self._color = QColor(255, 0, 0, 102)  # default red, ~40% opacity
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.hide()

    def set_style(self, color: str, opacity: float):
        """Update the box color and opacity."""
        c = QColor(color)
        c.setAlphaF(max(0.0, min(1.0, opacity)))
        self._color = c
        self._update_style()

    def _update_style(self):
        r, g, b, a = self._color.red(), self._color.green(), self._color.blue(), self._color.alpha()
        self.setStyleSheet(f"background-color: rgba({r},{g},{b},{a});")

    def place(self, x: int, y: int, w: int, h: int):
        """Position and resize the box relative to the overlay window."""
        self.setGeometry(x, y, max(1, w), max(1, h))
        self._update_style()


class GameOverlay:
    """Transparent overlay window for the League of Legends game.

    Provides show/hide methods for each HUD element overlay box.
    All positions are automatically scaled based on game window size,
    DPI, GlobalScale, and MinimapScale.
    """

    # Poll interval for game window tracking (ms)
    POLL_INTERVAL_MS = 100

    def __init__(self, live_client: LiveClient, config_monitor: LiveClientConfigMonitor):
        self._live_client = live_client
        self._config_monitor = config_monitor
        self._user = User()

        self._window: QWidget | None = None
        self._timer: QTimer | None = None

        # Overlay boxes keyed by element name
        self._boxes: dict[str, _OverlayBox] = {}
        # Track which elements are enabled and their params
        self._enabled: dict[str, dict] = {}

        # Cache last known window rect to avoid redundant updates
        self._last_rect: tuple[int, int, int, int] | None = None
        self._last_global_scale: float | None = None
        self._last_minimap_scale: float | None = None
        self._last_flip: bool | None = None

    def start(self):
        """Initialize and show the overlay. Must be called after QApplication is created."""
        if self._window is not None:
            return

        self._window = QWidget()
        self._window.setWindowTitle("LoQ Overlay")

        # Frameless, always-on-top, transparent, tool window (no taskbar icon)
        self._window.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
            | Qt.WindowType.WindowTransparentForInput
        )

        self._window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self._window.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self._window.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating, True)

        self._window.show()
        self._window.raise_()
        self._window.activateWindow()

        # Set Win32 click-through extended style
        self._set_click_through()

        # Create all overlay boxes
        self._create_boxes()

        # Start polling timer
        self._timer = QTimer()
        self._timer.timeout.connect(self._poll)
        self._timer.start(self.POLL_INTERVAL_MS)

    def stop(self):
        """Stop and hide the overlay."""
        if self._timer:
            self._timer.stop()
            self._timer = None

        if self._window:
            self._window.hide()
            self._window.deleteLater()
            self._window = None

        self._boxes.clear()
        self._enabled.clear()
        self._last_rect = None

    # -- Abilities (1=Q, 2=W, 3=E, 4=R) --

    def show_ability(self, ability: int, color: str = "#FF0000", opacity: float = 0.4):
        """Show overlay on an ability slot. ability: 1=Q, 2=W, 3=E, 4=R."""
        key = f"ability_{ability}"
        self._enabled[key] = {"color": color, "opacity": opacity}
        self._update_box(key)

    def hide_ability(self, ability: int):
        """Hide overlay on an ability slot."""
        key = f"ability_{ability}"
        self._enabled.pop(key, None)
        if key in self._boxes:
            self._boxes[key].hide()

    # -- Summoner spells (1=D, 2=F) --

    def show_summoner_spell(self, spell: int, color: str = "#FF0000", opacity: float = 0.4):
        """Show overlay on a summoner spell. spell: 1=D, 2=F."""
        key = f"spell_{spell}"
        self._enabled[key] = {"color": color, "opacity": opacity}
        self._update_box(key)

    def hide_summoner_spell(self, spell: int):
        """Hide overlay on a summoner spell."""
        key = f"spell_{spell}"
        self._enabled.pop(key, None)
        if key in self._boxes:
            self._boxes[key].hide()

    # -- Recall --

    def show_recall(self, color: str = "#FF0000", opacity: float = 0.4):
        """Show overlay on the recall button."""
        self._enabled["recall"] = {"color": color, "opacity": opacity}
        self._update_box("recall")

    def hide_recall(self):
        """Hide overlay on the recall button."""
        self._enabled.pop("recall", None)
        if "recall" in self._boxes:
            self._boxes["recall"].hide()

    # -- Trinket --

    def show_trinket(self, color: str = "#FF0000", opacity: float = 0.4):
        """Show overlay on the trinket slot."""
        self._enabled["trinket"] = {"color": color, "opacity": opacity}
        self._update_box("trinket")

    def hide_trinket(self):
        """Hide overlay on the trinket slot."""
        self._enabled.pop("trinket", None)
        if "trinket" in self._boxes:
            self._boxes["trinket"].hide()

    # -- Health bar --

    def show_health(
        self,
        start_pct: float = 0.0,
        end_pct: float = 1.0,
        color: str = "#FF0000",
        opacity: float = 0.4,
    ):
        """Show overlay on the health bar. start_pct/end_pct define the span (0.0 to 1.0)."""
        self._enabled["health"] = {
            "color": color,
            "opacity": opacity,
            "start_pct": start_pct,
            "end_pct": end_pct,
        }
        self._update_box("health")

    def hide_health(self):
        """Hide overlay on the health bar."""
        self._enabled.pop("health", None)
        if "health" in self._boxes:
            self._boxes["health"].hide()

    # -- Resource bar --

    def show_resource(
        self,
        start_pct: float = 0.0,
        end_pct: float = 1.0,
        color: str = "#FF0000",
        opacity: float = 0.4,
    ):
        """Show overlay on the resource bar. start_pct/end_pct define the span (0.0 to 1.0)."""
        self._enabled["resource"] = {
            "color": color,
            "opacity": opacity,
            "start_pct": start_pct,
            "end_pct": end_pct,
        }
        self._update_box("resource")

    def hide_resource(self):
        """Hide overlay on the resource bar."""
        self._enabled.pop("resource", None)
        if "resource" in self._boxes:
            self._boxes["resource"].hide()

    # -- Minimap --

    def show_minimap(self, color: str = "#FF0000", opacity: float = 0.4):
        """Show overlay on the minimap."""
        self._enabled["minimap"] = {"color": color, "opacity": opacity}
        self._update_box("minimap")

    def hide_minimap(self):
        """Hide overlay on the minimap."""
        self._enabled.pop("minimap", None)
        if "minimap" in self._boxes:
            self._boxes["minimap"].hide()

    # -- Internal methods --

    def _set_click_through(self):
        """Set Win32 extended style to make the window click-through."""
        if not self._window:
            return

        hwnd = int(self._window.winId())
        style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        ctypes.windll.user32.SetWindowLongW(
            hwnd, GWL_EXSTYLE, style | WS_EX_TRANSPARENT | WS_EX_LAYERED
        )

    def _create_boxes(self):
        """Pre-create all overlay box widgets."""
        if not self._window:
            return

        # 4 abilities
        for i in range(1, 5):
            self._boxes[f"ability_{i}"] = _OverlayBox(self._window)

        # 2 summoner spells
        for i in range(1, 3):
            self._boxes[f"spell_{i}"] = _OverlayBox(self._window)

        # Single elements
        for name in ("recall", "trinket", "health", "resource", "minimap"):
            self._boxes[name] = _OverlayBox(self._window)

    def _poll(self):
        """Periodic check: update overlay position/visibility based on game window state."""
        if not self._window:
            return

        is_focused = self._live_client.is_focused()
        print(f"Poll: is_focused={is_focused}")

        if not is_focused:
            if self._window.isVisible():
                self._window.hide()
            return

        rect = self._live_client.get_window_rect()
        print(f"Poll: rect={rect}")
        if not rect:
            if self._window.isVisible():
                self._window.hide()
            return

        # Show overlay if game is focused
        if not self._window.isVisible():
            self._window.show()
            self._set_click_through()
            print("Poll: Window shown")

        config = self._config_monitor.get_config()
        global_scale = config.game.GlobalScale if config else 0.0
        minimap_scale = config.game.MinimapScale if config else 1.0
        flip = bool(config.game.FlipMiniMap) if config else False

        print(f"Poll: global_scale={global_scale}, minimap_scale={minimap_scale}, flip={flip}")

        # Check if anything changed that requires repositioning
        if (
            rect != self._last_rect
            or global_scale != self._last_global_scale
            or minimap_scale != self._last_minimap_scale
            or flip != self._last_flip
        ):
            self._last_rect = rect
            self._last_global_scale = global_scale
            self._last_minimap_scale = minimap_scale
            self._last_flip = flip

            dpi_scale = self._user.get_dpi_scale()
            wx, wy, ww, wh = rect

            print(f"Poll: dpi_scale={dpi_scale}, window geo=({wx}, {wy}, {ww}, {wh})")

            # Resize overlay window to match game window (use physical pixels)
            self._window.setGeometry(wx, wy, ww, wh)

            print(
                f"Poll: overlay window geo=({self._window.x()}, {self._window.y()}, {self._window.width()}, {self._window.height()})"
            )

            # Reposition all enabled boxes
            self._update_all_boxes()

    def _update_all_boxes(self):
        """Reposition all currently enabled overlay boxes."""
        for key in self._enabled:
            self._update_box(key)

    def _update_box(self, key: str):
        """Compute and apply position for a single overlay box."""
        if not self._window or key not in self._boxes:
            return

        box = self._boxes[key]

        if key not in self._enabled:
            box.hide()
            return

        params = self._enabled[key]
        rect = self._last_rect
        if not rect:
            return

        config = self._config_monitor.get_config()
        global_scale = config.game.GlobalScale if config else 0.0
        minimap_scale = config.game.MinimapScale if config else 1.0
        flip = bool(config.game.FlipMiniMap) if config else False
        dpi_scale = self._user.get_dpi_scale()
        wx, wy, ww, wh = rect

        # Compute absolute screen rect for the element
        if key == "minimap":
            abs_x, abs_y, w, h = compute_minimap_rect(
                global_scale=global_scale,
                minimap_scale=minimap_scale,
                window_x=wx,
                window_y=wy,
                window_width=ww,
                window_height=wh,
                dpi_scale=dpi_scale,
                flip_minimap=flip,
            )
        else:
            bounds = self._get_bounds(key)
            if bounds is None:
                return

            start_pct = params.get("start_pct", 0.0)
            end_pct = params.get("end_pct", 1.0)

            abs_x, abs_y, w, h = compute_element_rect(
                element_bounds=bounds,
                global_scale=global_scale,
                window_x=wx,
                window_y=wy,
                window_width=ww,
                window_height=wh,
                dpi_scale=dpi_scale,
                start_pct=start_pct,
                end_pct=end_pct,
            )

        # Convert absolute screen coords to overlay-window-relative coords
        overlay_x = self._window.x()
        overlay_y = self._window.y()
        rel_x = abs_x - overlay_x
        rel_y = abs_y - overlay_y

        box.set_style(params["color"], params["opacity"])
        box.place(rel_x, rel_y, w, h)
        box.show()
        print(f"Update box {key}: rel=({rel_x}, {rel_y}, {w}, {h})")

    def _get_bounds(self, key: str):
        """Look up the HudElementBounds or BarElementBounds for a key."""
        if key.startswith("ability_"):
            idx = int(key.split("_")[1])
            return ABILITY_BOUNDS.get(idx)
        elif key.startswith("spell_"):
            idx = int(key.split("_")[1])
            return SUMMONER_SPELL_BOUNDS.get(idx)
        elif key == "recall":
            return RECALL_BOUNDS
        elif key == "trinket":
            return TRINKET_BOUNDS
        elif key == "health":
            return HEALTH_BOUNDS
        elif key == "resource":
            return RESOURCE_BOUNDS
        return None
