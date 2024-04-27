from .restriction_base import RestrictionBase
from ..manager.disable_manager import DisableManager


class DisableHotkeyBase(RestrictionBase):
    disable_hotkeys: dict

    @classmethod
    def init(cls):
        cls.disable_manager = DisableManager()

    @classmethod
    def restriction_content(cls):
        cls.enable_type(False)

    @classmethod
    def on_end(cls):
        cls.enable_type(True)
        del cls.disable_manager

    @classmethod
    def enable_type(cls, enable: bool):
        cls.disable_manager.enable_type(enable, cls.disable_hotkeys)
