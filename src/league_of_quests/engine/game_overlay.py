from ..ui import GameOverlayWindow
from ..core import HotkeyType
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

        self.window.hide()

    def show_aility_cover(self, ability: HotkeyType):
        widget = self._hotkey_to_widget.get(ability)
        if widget:
            widget.show()

    def hide_aility_cover(self, ability: HotkeyType):
        widget = self._hotkey_to_widget.get(ability)
        if widget:
            widget.hide()

    def show_health_cover(self, from_pct: float, to_pct: float):
        pass

    def hide_health_cover(self):
        pass

    def show_resource_cover(self, from_pct: float, to_pct: float):
        pass

    def hide_resource_cover(self):
        pass

    def show_map_cover(self):
        self.window.map.show()

    def hide_map_cover(self):
        self.window.map.hide()

    def _update_overlay(self):
        is_focused = self._live_client.is_focused()
        if not is_focused:
            self.window.hide()
            return

        self._update_overlay_window()
        self._update_covers()
        self.window.show()

    def _update_overlay_window(self):
        rect = self._live_client.get_window_rect()
        if not rect:
            return

        self.window.move(rect[0], rect[1])
        self.window.resize(rect[2], rect[3])

    def _update_covers(self):
        pass
