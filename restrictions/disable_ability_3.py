from .disable_hotkey_base import DisableAbilityBase
from ..utils.constants import ABILITY3


class DisableAbility3(DisableAbilityBase):
    title = "Ultimate is locked!"
    difficulty = 1
    ability_num = [3]
    attributes = [ABILITY3]
