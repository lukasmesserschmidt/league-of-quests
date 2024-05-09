from contextlib import suppress
import keyboard

from .hotkey_manager import HotkeyManager
from ..lol_data.lol_settings import LolSettings
from ..gui.game_overlay.game_overlay_window import get_game_overlay
from ..lol_data.lol_window_data import LolWindowData


class DisableManager:
    def __init__(self):
        self.hotkey_manager = HotkeyManager()

    def enable_type(self, enable: bool, disable_types: dict[str : list[int]]):
        self.hotkey_manager.set_hotkeys("enable", disable_types, enable)
        get_game_overlay().enable_cover(not enable, disable_types)
