from .hotkey_manager import HotkeyManager
from ..gui.game_overlay.game_overlay_window import get_game_overlay


class DisableManager:
    def __init__(self):
        self.hotkey_manager = HotkeyManager()

    def enable_hotkey(self, enable: bool, disable_hotkeys: dict[str, list[int]]):
        self.hotkey_manager.hotkey_event("enable", disable_hotkeys, enable)
        get_game_overlay().enable_cover(not enable, disable_hotkeys)
