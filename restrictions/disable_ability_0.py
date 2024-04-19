from .disable_hotkey_base import DisableAbilityBase
from ..utils.constants import ABILITY0


class DisableAbility0(DisableAbilityBase):
    title = "Ability 1 is locked!"
    difficulty = 0
    ability_num = [0]
    attributes = [ABILITY0]
