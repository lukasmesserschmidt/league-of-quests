from contextlib import suppress
from PySide6.QtCore import QTimer
import keyboard

from ..lol_data.lol_settings import LolSettings
from ..lol_data.lol_window_data import LolWindowData
from ..utils.is_game_active import is_game_active
from ..utils.constants import Constants


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

            with suppress(Exception):
                hotkeys = LolSettings.get_hotkeys(
                    cls.hotkey_types.get(Constants.DISABLE)
                )
                cls._disable(*hotkeys)

            with suppress(Exception):
                hotkeys = LolSettings.get_hotkeys(cls.hotkey_types.get(Constants.REMAP))
                cls._remap(*hotkeys)

            with suppress(Exception):
                hotkeys = LolSettings.get_hotkeys(cls.hotkey_types.get(Constants.PRESS))
                cls._press(*hotkeys)

            with suppress(Exception):
                hotkeys = LolSettings.get_hotkeys(
                    cls.hotkey_types.get(Constants.PRESS_RELEASE)
                )
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
        for hotkey_type, args in hotkey_types.items():
            hotkeys = [(hotkey_type, arg) for arg in args]

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
    def _press_release(cls, *args: str):
        for arg in args:
            with suppress(Exception):
                keyboard.press_and_release(arg)

    @classmethod
    def _remap(cls, *args: tuple[str, str]):
        for arg in args:
            with suppress(Exception):
                keyboard.remap_key(arg[0], arg[1])
