from contextlib import suppress
import keyboard
from enum import Enum

from ..lol_data.lol_settings import LolSettings
from ..lol_data.lol_window_data import LolWindowData
from ..utils.is_game_active import is_game_active


class EventType(Enum):
    ENABLE = "enable"
    PRESS = "press"
    REMAP = "remap"
    PRESS_RELEASE = "press_release"


class HotkeyManager:
    def __init__(self):
        self.event_types = {
            EventType.ENABLE: {"reset": True, "last": [], "func": self._enable},
            EventType.REMAP: {"reset": False, "last": [], "func": self._remap},
            EventType.PRESS: {"reset": False, "last": [], "func": self._press},
            EventType.PRESS_RELEASE: {"func": self._press_release},
        }

    def hotkey_event(
        self, event_type: str, hotkey_types: dict[str, list[int]], enable: bool = None
    ):
        if LolWindowData.lol_is_top and is_game_active():
            event_type = self.event_types.get(event_type)
            event_func = event_type.get("func")
            current_hotkeys = LolSettings.get_hotkeys(hotkey_types)

            if enable is not None and "reset" in event_type:
                reset = event_type.get("reset")
                last_hotkeys = event_type.get("last")

                event_func(reset, *last_hotkeys)
                event_type["last"] = current_hotkeys

                event_func(enable, *current_hotkeys)
            else:
                event_func(*current_hotkeys)
        else:
            keyboard.unhook_all()

    def _enable(self, enable: bool, *args: str):
        for arg in args:
            with suppress(Exception):
                if enable:
                    keyboard.unblock_key(arg)
                else:
                    keyboard.block_key(arg)

    def _press(self, press: bool, *args: str):
        for arg in args:
            with suppress(Exception):
                if press:
                    if not (arg == "F4" and keyboard.is_pressed("alt")):
                        keyboard.press(arg)
                else:
                    keyboard.release(arg)

    def _press_release(self, *args):
        for arg in args:
            with suppress(Exception):
                keyboard.press_and_release(arg)

    def _remap(self, enable: bool, *args):
        for arg in args:
            with suppress(Exception):
                if enable:
                    keyboard.remap_key(arg[0], arg[1])
                else:
                    keyboard.unhook_key(arg[0])
