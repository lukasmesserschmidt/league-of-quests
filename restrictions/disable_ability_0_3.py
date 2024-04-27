from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import ABILITY0, ABILITY1, ABILITY2, ABILITY3


class DisableAbility0(DisableHotkeyBase):
    title = "Ability 1 is disabled!"
    difficulty = 0
    disable_hotkeys = {"ability": [0]}
    attributes = [ABILITY0]


class DisableAbility1(DisableHotkeyBase):
    title = "Ability 2 is disabled!"
    difficulty = 0
    disable_hotkeys = {"ability": [1]}
    attributes = [ABILITY1]


class DisableAbility2(DisableHotkeyBase):
    title = "Ability 3 is disabled!"
    difficulty = 0
    disable_hotkeys = {"ability": [2]}
    attributes = [ABILITY2]


class DisableAbility3(DisableHotkeyBase):
    title = "Ultimate is disabled!"
    difficulty = 1
    disable_hotkeys = {"ability": [3]}
    attributes = [ABILITY3]
