from PySide6.QtWidgets import QWidget

from ..ui import GameOverlayWindow
from ..data import HotkeyType
from ..platform import LiveClient


class GameOverlay:
    def __init__(self):
        self._live_client = LiveClient()

        self.window = GameOverlayWindow()

        self._hotkey_to_widget = {
            HotkeyType.ABILITY_1: self.window.ability_1,
            HotkeyType.ABILITY_2: self.window.ability_2,
            HotkeyType.ABILITY_3: self.window.ability_3,
            HotkeyType.ABILITY_4: self.window.ability_4,
            HotkeyType.SUMMONER_SPELL_1: self.window.summoner_spell_1,
            HotkeyType.SUMMONER_SPELL_2: self.window.summoner_spell_2,
            HotkeyType.TRINKET: self.window.trinket,
            HotkeyType.RECALL: self.window.recall,
        }

        self._cover_ref_counts: dict[QWidget, int] = {}

    def show_aility_cover(self, ability: HotkeyType):
        widget = self._hotkey_to_widget.get(ability)
        self._show_cover(widget)

    def hide_aility_cover(self, ability: HotkeyType):
        widget = self._hotkey_to_widget.get(ability)
        self._hide_cover(widget)

    def show_health_cover(self, from_pct: float, to_pct: float):
        widget = self.window.health
        self.window.set_health_span(from_pct, to_pct)
        self._show_cover(widget)

    def hide_health_cover(self):
        widget = self.window.health
        self._hide_cover(widget)

    def show_resource_cover(self, from_pct: float, to_pct: float):
        widget = self.window.resource
        self.window.set_resource_span(from_pct, to_pct)
        self._show_cover(widget)

    def hide_resource_cover(self):
        widget = self.window.resource
        self._hide_cover(widget)

    def show_map_cover(self):
        widget = self.window.map
        self._show_cover(widget)

    def hide_map_cover(self):
        widget = self.window.map
        self._hide_cover(widget)

    def _show_cover(self, widget: QWidget | None):
        if widget is None:
            return

        if widget not in self._cover_ref_counts:
            self._cover_ref_counts[widget] = 0
        self._cover_ref_counts[widget] += 1

        if self._cover_ref_counts[widget] == 1:
            widget.show()

    def _hide_cover(self, widget: QWidget | None):
        if widget is None:
            return

        if widget not in self._cover_ref_counts:
            return

        self._cover_ref_counts[widget] -= 1

        if self._cover_ref_counts[widget] <= 0:
            del self._cover_ref_counts[widget]
            widget.hide()
