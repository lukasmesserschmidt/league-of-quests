from random import randint

from .restriction_disable_hotkey_base import RestrictionDisableHotkeyBase
from ..utils.constants import Constants


class DisableAbility(RestrictionDisableHotkeyBase):
    title = "Ability ? is disabled!"
    difficulty = 0
    attributes = [Constants.ABILITY]

    hotkey_types = {Constants.ABILITY: []}

    @classmethod
    def init(cls):
        super().init()
        rand_ability = randint(0, 2)
        cls.set_hotkey_types((Constants.ABILITY, [rand_ability]))

        cls.title = f"Ability {rand_ability + 1} is disabled!"
