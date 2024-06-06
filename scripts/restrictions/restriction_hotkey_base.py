from .restriction_base import RestrictionBase
from ..manager.hotkey_manager import HotkeyManager
from ..utils.constants import Constants


class RestrictionHotkeyBase(RestrictionBase):
    hotkey_types: dict[Constants, list[int | tuple[int, float | int]]]

    @classmethod
    def hotkey_event(
        cls,
        event_type: Constants,
        hotkey_types: dict[Constants, list[int]],
        enable: bool = None,
    ):
        HotkeyManager.hotkey_event(event_type, hotkey_types, enable)

    @classmethod
    def set_hotkey_types(
        cls, *args: tuple[Constants, list[int | tuple[int, float | int]]]
    ):
        for hotkey_types in args:
            hotkey_type = hotkey_types[0]
            hotkey_nums = hotkey_types[1]

            cls.hotkey_types[hotkey_type] = hotkey_nums
