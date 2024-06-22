"""
This module contains the RestrictionHotkeyBase class.
"""

from .restriction_base import RestrictionBase
from ..manager.hotkey_manager import HotkeyManager
from ..utils.constants import Constants


class RestrictionHotkeyBase(RestrictionBase):
    """
    A base class for all restrictions that use hotkeys.
    """

    # deffine hotkey types
    hotkey_types: dict[Constants, list[int | tuple[int, float | int]]]

    @classmethod
    def hotkey_event(
        cls,
        event_type: Constants,
        hotkey_types: dict[Constants, list[int]],
        enable: bool = None,
    ):
        """
        Enables or disables the given hotkey types in the given event type.
        """
        HotkeyManager.hotkey_event(event_type, hotkey_types, enable, cls)

    @classmethod
    def set_hotkey_types(
        cls, *args: tuple[Constants, list[int | tuple[int, float | int]]]
    ):
        """
        Sets the hotkey types.
        """
        for hotkey_types in args:
            hotkey_type = hotkey_types[0]
            hotkey_nums = hotkey_types[1]

            cls.hotkey_types[hotkey_type] = hotkey_nums
