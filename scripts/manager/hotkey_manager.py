from contextlib import suppress
from PySide6.QtCore import QTimer
import keyboard

from ..lol_data.lol_settings import LolSettings
from ..lol_data.lol_window_data import LolWindowData
from ..utils.is_game_active import is_game_active
from ..utils.constants import Constants


# class HotkeyManager:
#     def __init__(self):
#         self.event_types = {
#             Constants.ENABLE: {"reset": True, "last": [], "func": self._enable},
#             Constants.REMAP: {"reset": False, "last": [], "func": self._remap},
#             Constants.PRESS: {"reset": False, "last": [], "func": self._press},
#             Constants.PRESS_RELEASE: {"func": self._press_release},
#         }

#     def hotkey_event(
#         self,
#         event_type: Constants,
#         hotkey_types: dict[Constants, list[int]],
#         enable: bool = None,
#     ):
#         if LolWindowData.lol_is_top and is_game_active():
#             event_type = self.event_types.get(event_type)
#             event_func = event_type.get("func")
#             current_hotkeys = LolSettings.get_hotkeys(hotkey_types)

#             if enable is not None and "reset" in event_type:
#                 reset = event_type.get("reset")
#                 last_hotkeys = event_type.get("last")

#                 event_func(reset, *last_hotkeys)
#                 event_type["last"] = current_hotkeys

#                 event_func(enable, *current_hotkeys)
#             else:
#                 event_func(*current_hotkeys)
#         else:
#             keyboard.unhook_all()

#     def _enable(self, enable: bool, *args: str):
#         for arg in args:
#             with suppress(Exception):
#                 if enable:
#                     keyboard.unblock_key(arg)
#                 else:
#                     keyboard.block_key(arg)

#     def _press(self, press: bool, *args: str):
#         for arg in args:
#             with suppress(Exception):
#                 if press:
#                     if not (arg == "F4" and keyboard.is_pressed("alt")):
#                         keyboard.press(arg)
#                 else:
#                     keyboard.release(arg)

#     def _press_release(self, *args):
#         for arg in args:
#             with suppress(Exception):
#                 keyboard.press_and_release(arg)

#     def _remap(self, enable: bool, *args):
#         for arg in args:
#             with suppress(Exception):
#                 if enable:
#                     keyboard.remap_key(arg[0], arg[1])
#                 else:
#                     keyboard.unhook_key(arg[0])


class HotkeyManager:
    hotkey_types = {
        Constants.DISABLE: set(),
        Constants.REMAP: set(),
        Constants.PRESS: set(),
        Constants.PRESS_RELEASE: set(),
    }

    main_loop_timer = None

    @classmethod
    def start(cls):
        if cls.main_loop_timer is None:
            cls.main_loop_timer = QTimer()
            cls.main_loop_timer.timeout.connect(cls.main_loop)

        cls.main_loop_timer.start(200)

    @classmethod
    def stop(cls):
        if cls.main_loop_timer is not None:
            cls.main_loop_timer.stop()
            for event_type in cls.hotkey_types:
                cls.hotkey_types[event_type].clear()

    @classmethod
    def main_loop(cls):
        if LolWindowData.lol_is_top and is_game_active():
            keyboard.unhook_all()

            hotkeys = cls.hotkey_types.get(Constants.DISABLE)
            cls._disable(*hotkeys)

            hotkeys = cls.hotkey_types.get(Constants.REMAP)
            cls._remap(*hotkeys)

            hotkeys = cls.hotkey_types.get(Constants.PRESS)
            cls._press(*hotkeys)

            hotkeys = cls.hotkey_types.get(Constants.PRESS_RELEASE)
            cls._press_release(*hotkeys)
            cls.hotkey_types[Constants.PRESS_RELEASE].clear()
        else:
            keyboard.unhook_all()

    @classmethod
    def hotkey_event(
        cls,
        event_type: Constants,
        hotkey_types: dict[Constants, list[int]],
        enable: bool = None,
    ):
        hotkeys = LolSettings.get_hotkeys(hotkey_types)

        if enable or enable is None:
            cls.hotkey_types[event_type].update(hotkeys)
        else:
            cls.hotkey_types[event_type].difference_update(hotkeys)

    @classmethod
    def _disable(cls, *args: str):
        for arg in args:
            with suppress(Exception):
                keyboard.block_key(arg)

    @classmethod
    def _press(cls, *args: str):
        for arg in args:
            with suppress(Exception):
                if not (arg == "F4" and keyboard.is_pressed("alt")):
                    keyboard.press(arg)

    @classmethod
    def _press_release(cls, *args):
        for arg in args:
            with suppress(Exception):
                keyboard.press_and_release(arg)

    @classmethod
    def _remap(cls, *args):
        for arg in args:
            with suppress(Exception):
                keyboard.remap_key(arg[0], arg[1])
