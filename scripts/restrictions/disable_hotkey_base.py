from .restriction_base import RestrictionBase
from ..manager.disable_manager import DisableManager
from ..utils.constants import Constants


class DisableHotkeyBase(RestrictionBase):
    disable_hotkeys: dict[Constants, list[int]]

    @classmethod
    def init(cls):
        cls.disable_manager = DisableManager()

    @classmethod
    def restriction_content(cls):
        cls.enable_hotkey(False)

    @classmethod
    def on_end(cls):
        cls.enable_hotkey(True)
        del cls.disable_manager

    @classmethod
    def enable_hotkey(cls, enable: bool):
        cls.disable_manager.enable_hotkey(enable, cls.disable_hotkeys)
