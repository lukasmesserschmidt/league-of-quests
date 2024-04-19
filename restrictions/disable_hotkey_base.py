from .restriction_base import RestrictionBase
from ..manager.hotkey_manager import HotkeyManager


class DisableAbilityBase(RestrictionBase):
    ability_num: list[int]

    @classmethod
    def on_loop_end(cls):
        HotkeyManager.enable_ability(True, *cls.ability_num)

    @classmethod
    def restriction_content(cls):
        HotkeyManager.enable_ability(False, *cls.ability_num)
