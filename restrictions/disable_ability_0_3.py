from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import ABILITY0, ABILITY1, ABILITY2, ABILITY3


class DisableAbility0(DisableHotkeyBase):
    title = "Ability 1 is disabled!"
    difficulty = 0
    ability_num = [0]
    hotkey_type = "ability"
    attributes = [ABILITY0]


class DisableAbility1(DisableHotkeyBase):
    title = "Ability 2 is disabled!"
    difficulty = 0
    ability_num = [1]
    hotkey_type = "ability"
    attributes = [ABILITY1]


class DisableAbility2(DisableHotkeyBase):
    title = "Ability 3 is disabled!"
    difficulty = 0
    ability_num = [2]
    hotkey_type = "ability"
    attributes = [ABILITY2]


class DisableAbility3(DisableHotkeyBase):
    title = "Ultimate is disabled!"
    difficulty = 1
    ability_num = [3]
    hotkey_type = "ability"
    attributes = [ABILITY3]
