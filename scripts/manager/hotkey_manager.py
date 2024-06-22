"""
This module contains the HotkeyManager class.
"""

import time

from contextlib import suppress
from PySide6.QtCore import QTimer
import keyboard

from ..lol_data.lol_settings import LolSettings
from ..lol_data.lol_window_data import LolWindowData
from ..utils.is_game_active import is_game_active
from ..utils.constants import Constants


class HotkeyManager:
    """
    A class for managing hotkeys.
    """

    # init hotkey types dict
    hotkey_types_dict = {
        Constants.DISABLE: set(),
        Constants.REMAP: set(),
        Constants.PRESS: set(),
        Constants.PRESS_RELEASE: set(),
    }

    # init variables
    update_hotkeys_loop_timer = None

    # control
    @classmethod
    def start(cls):
        """
        Start the update hotkeys loop timer.
        """
        if cls.update_hotkeys_loop_timer is None:
            cls.update_hotkeys_loop_timer = QTimer()
            cls.update_hotkeys_loop_timer.timeout.connect(cls._update_hotkeys)

        cls.update_hotkeys_loop_timer.start(100)

    @classmethod
    def stop(cls):
        """
        Stop the update hotkeys loop timer and clear all hotkey numbers in the hotkey types dictionary.
        """
        if cls.update_hotkeys_loop_timer is not None:
            cls.update_hotkeys_loop_timer.stop()
            for hotkey_nums in cls.hotkey_types_dict.values():
                hotkey_nums.clear()

    # update hotkeys loop
    @classmethod
    def _update_hotkeys(cls):
        if LolWindowData.lol_is_top and is_game_active():
            keyboard.unhook_all()

            for event, handler in [
                (Constants.DISABLE, cls._disable),
                (Constants.REMAP, cls._remap),
                (Constants.PRESS, cls._press),
                (Constants.PRESS_RELEASE, cls._press_release),
            ]:
                with suppress(Exception):
                    hotkeys = cls._get_hotkeys(cls.hotkey_types_dict.get(event))
                    handler(*hotkeys)
        else:
            keyboard.unhook_all()

    # events
    @classmethod
    def hotkey_event(
        cls,
        event_type: Constants,
        hotkey_types: dict[Constants, list[int | tuple[int, int]]],
        enable: bool = None,
        owner: object = None,
    ):
        """
        Updates the `hotkey_types_dict` with the provided `hotkey_types` for the given `event_type`.

        Args:
            event_type (Constants): The type of event for which the hotkeys are being updated.
            hotkey_types (dict[Constants, list[int | tuple[int, int]]]): A dictionary mapping `hotkey_type` to a list of hotkeys.
            enable (bool, optional): If `True`, adds the hotkeys to `hotkey_types_dict`. If `False`, removes the hotkeys from `hotkey_types_dict`. Defaults to `None`.
            owner (object, optional): The owner of the hotkeys. Defaults to `None`.
        """
        for hotkey_type, args in hotkey_types.items():
            hotkeys = [(hotkey_type, arg, owner) for arg in args]

            if enable or enable is None:
                cls.hotkey_types_dict[event_type].update(hotkeys)
            else:
                cls.hotkey_types_dict[event_type].difference_update(hotkeys)

    @classmethod
    def write_chat(cls, text: str):
        """
        Writes the given text to the chat window if the League of Legends window is active.
        """
        if LolWindowData.lol_is_top and is_game_active():
            keyboard.press_and_release("enter")
            time.sleep(0.05)
            keyboard.write(text)
            time.sleep(0.05)
            keyboard.press_and_release("enter")

    # event types
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
                    keyboard.release(arg)
                    keyboard.press(arg)

    @classmethod
    def _press_release(cls, *args: str):
        for arg in args:
            with suppress(Exception):
                keyboard.press_and_release(arg)
        cls.hotkey_types_dict[Constants.PRESS_RELEASE].clear()

    @classmethod
    def _remap(cls, *args: list[str, str]):
        for arg in args:
            with suppress(Exception):
                keyboard.remap_key(arg[0], arg[1])

    # utils
    @classmethod
    def _get_hotkeys(cls, hotkey_types_set: set[tuple[Constants, int | tuple[int]]]):
        hotkeys = set()
        for hotkey_types in hotkey_types_set:
            hotkey_type = hotkey_types[0]
            hotkey_nums = hotkey_types[1]
            hotkey = cls._resolve_hotkey(hotkey_type, hotkey_nums)
            hotkeys.add(hotkey)

        return hotkeys

    @classmethod
    def _resolve_hotkey(cls, hotkey_type: Constants, hotkey_nums: int | tuple[int]):
        hotkey = None
        if isinstance(hotkey_nums, int):
            hotkey = LolSettings.get_lol_setting(hotkey_type, hotkey_nums)
        elif isinstance(hotkey_nums, tuple):
            hotkey = []
            for hotkey_num in hotkey_nums:
                hotkey.append(cls._resolve_hotkey(hotkey_type, hotkey_num))

            hotkey = tuple(hotkey)

        return hotkey
