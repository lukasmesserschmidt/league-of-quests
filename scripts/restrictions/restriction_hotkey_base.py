from .restriction_base import RestrictionBase
from ..manager.hotkey_manager import HotkeyManager
from ..utils.constants import Constants


class RestrictionHotkeyBase(RestrictionBase):
    hotkey_types: dict[str, list[int]]

    @classmethod
    def hotkey_event(
        cls,
        event_type: Constants,
        hotkey_types: dict[Constants, list[int]],
        enable: bool = None,
    ):
        HotkeyManager.hotkey_event(event_type, hotkey_types, enable)
