from contextlib import suppress
import keyboard

from ..lol_data.lol_settings import LolSettings
from ..gui.game_overlay.game_overlay_window import get_game_overlay
from ..lol_data.lol_window_data import LolWindowData


class DisableManager:
    def __init__(self):
        self.last_hotkeys = []

    def enable_key(self, enable: bool, *args: int):
        for arg in args:
            with suppress(Exception):
                if enable:
                    keyboard.unblock_key(arg)
                else:
                    keyboard.block_key(arg)

    def enable_type(self, enable: bool, disable_hotkeys: dict[str : list[int]]):
        if LolWindowData.lol_is_top:
            current_hotkeys = []

            self.enable_key(True, *self.last_hotkeys)
            for hotkey_type, args in disable_hotkeys.items():
                hotkeys = LolSettings.get_hotkeys(hotkey_type, *args)

                self.enable_key(enable, *hotkeys)
                get_game_overlay().enable_cover(not enable, hotkey_type, *args)

                current_hotkeys.extend(hotkeys)

            self.last_hotkeys = current_hotkeys
        else:
            keyboard.unhook_all()
            for hotkey_type, args in disable_hotkeys.items():
                get_game_overlay().enable_cover(False, hotkey_type, *args)
