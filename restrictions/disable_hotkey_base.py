from .restriction_base import RestrictionBase
from ..manager.disable_manager import DisableManager


class DisableHotkeyBase(RestrictionBase):
    ability_num: list[int]
    hotkey_type: str

    @classmethod
    def restriction_content(cls):
        cls.enable_type(False)

    @classmethod
    def on_end(cls):
        cls.enable_type(True)

    @classmethod
    def enable_type(cls, enable: bool):
        DisableManager.enable_type(enable, cls.hotkey_type, *cls.ability_num)
