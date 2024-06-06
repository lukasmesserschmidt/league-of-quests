from PySide6.QtCore import Qt, QTimer

from .map_cover import MapCover
from .ability_cover import AbilityCover
from .summoner_spell_cover import SummonerSpellCover
from .resource_cover import ResourceCover
from .trinket_cover import TrinketCover
from .teleport_cover import TeleportCover
from ..window_base import WindowBase
from ...lol_data.lol_settings import LolSettings
from ...lol_data.lol_window_data import LolWindowData
from ...utils import user_data
from ...utils.is_game_active import is_game_active
from ...utils.is_program_active import is_program_active
from ...utils.constants import Constants


class GameOverlayWindow(WindowBase):
    def __init__(self):
        super().__init__()
        width, height = user_data.get_monitor_dpi_resolution()
        self.setGeometry(0, 0, width, height)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint
            | Qt.WindowTransparentForInput
            | Qt.FramelessWindowHint
        )

        self.overlay_covers = {
            Constants.ABILITY: {
                "active": set(),
                "reset": {0, 1, 2, 3},
                "cover": AbilityCover(self),
            },
            Constants.SUMMONER_SPELL: {
                "active": set(),
                "reset": {0, 1},
                "cover": SummonerSpellCover(self),
            },
            Constants.RESOURCE: {
                "active": set(),
                "reset": {0, 1},
                "percent": [(0, 0), (1, 0)],
                "cover": ResourceCover(self),
            },
            Constants.TRINKET: {
                "active": set(),
                "reset": {0},
                "cover": TrinketCover(self),
            },
            Constants.TELEPORT: {
                "active": set(),
                "reset": {0},
                "cover": TeleportCover(self),
            },
            Constants.MAP: {"active": set(), "reset": {0}, "cover": MapCover(self)},
        }

        self.main_loop_timer = QTimer(self)
        self.main_loop_timer.timeout.connect(self.main_loop)

        self.hide()

    def start(self):
        self.main_loop_timer.start(500)

    def stop(self):
        self.main_loop_timer.stop()
        for overlay_cover in self.overlay_covers.values():
            overlay_cover["active"].clear()
        self.hide()

    def main_loop(self):
        if (
            is_program_active()
            and is_game_active()
            and LolWindowData.lol_is_top
            and LolSettings.get_lol_setting(Constants.WINDOW_MODE) == 2
        ):
            self.update_covers()
            self.show()
        else:
            self.hide()

    def enable_cover(
        self,
        enable: bool,
        overlay_types: dict[Constants, list[int | tuple[int, float | int]]],
    ):
        for overlay_type, args in overlay_types.items():
            if overlay_type == Constants.RESOURCE:
                for arg in args:
                    self.overlay_covers[overlay_type]["percent"][arg[0]] = arg
                args = [arg[0] for arg in args]

            if enable:
                self.overlay_covers[overlay_type]["active"].update(args)
            else:
                self.overlay_covers[overlay_type]["active"].difference_update(args)

    def update_covers(self):
        for overlay_type, overlay_cover in self.overlay_covers.items():
            cover = overlay_cover["cover"]
            active_overlay = overlay_cover["active"]
            reset_overlay = overlay_cover.get("reset", set()).copy()
            reset_overlay.difference_update(active_overlay)

            if reset_overlay:
                cover.hide(*reset_overlay)
            if active_overlay:
                cover.show(*active_overlay)

            if overlay_type == Constants.RESOURCE:
                cover.set_percent(*overlay_cover["percent"])


def create_game_overlay():
    global game_overlay
    game_overlay = GameOverlayWindow()


def get_game_overlay():
    return game_overlay
