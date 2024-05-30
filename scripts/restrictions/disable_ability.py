from random import randint

from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import ABILITY
from ..utils.constants import Constants


class DisableAbility(DisableHotkeyBase):
    title = "Ability ? is disabled!"
    difficulty = 0
    attributes = [ABILITY]

    disable_hotkeys = {Constants.ABILITY: []}

    @classmethod
    def init(cls):
        super().init()
        rand_ability = randint(0, 2)
        cls.disable_hotkeys = {Constants.ABILITY: [rand_ability]}

        cls.title = f"Ability {rand_ability + 1} is disabled!"
