from contextlib import suppress
import keyboard

from ..lol_data.lol_settings import LolSettings
from ..lol_data.lol_window_data import LolWindowData


class HotkeyManager:
    def __init__(self):
        self.last_enable_hotkeys = []
        self.last_press_hotkeys = []

        self.set_types = {
            "enable": {"reset": True, "last": [], "func": self._enable_keys},
            "press": {"reset": False, "last": [], "func": self._press_hotkeys},
            "remap": {"reset": True, "last": [], "func": self._remap},
            "press_release": {"func": self._press_and_release},
        }

    def set_hotkeys(
        self, set_type: str, hotkey_types: dict[str, list[int]], enable: bool = None
    ):
        if LolWindowData.lol_is_top:
            set_type = self.set_types.get(set_type)
            set_func = set_type.get("func")
            current_hotkeys = LolSettings.get_hotkeys(hotkey_types)

            if enable != None and "reset" in set_type:
                reset = set_type.get("reset")
                last_hotkeys = set_type.get("last")

                set_func(reset, *last_hotkeys)
                set_type["last"] = current_hotkeys

                set_func(enable, *current_hotkeys)
            else:
                set_func(*current_hotkeys)
        else:
            keyboard.unhook_all()

    def _enable_keys(self, enable: bool, *args: str):
        for arg in args:
            with suppress(Exception):
                if enable:
                    keyboard.unblock_key(arg)
                else:
                    keyboard.block_key(arg)

    def _press_hotkeys(self, press: bool, *args: str):
        for arg in args:
            with suppress(Exception):
                if press:
                    keyboard.release(arg)
                    keyboard.press(arg)
                else:
                    keyboard.release(arg)

    def _press_and_release(self, *args):
        for arg in args:
            with suppress(Exception):
                keyboard.press_and_release(arg)

    def _remap(self, enable: bool, *args):
        for arg in args:
            with suppress(Exception):
                keyboard.unhook_key(arg[0])
            if enable:
                keyboard.remap_key(arg[0], arg[1])
