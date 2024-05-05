from random import randint

from .disable_hotkey_base import DisableHotkeyBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.attributes import ABILITY


class DisableAbility(DisableHotkeyBase):
    title = "Ability ? is disabled!"
    difficulty = 0
    attributes = [ABILITY]

    @classmethod
    def init(cls):
        super().init()
        rand_ability = randint(0, 2)
        cls.disable_types = {"ability": [rand_ability]}

        cls.title = f"Ability {rand_ability + 1} is disabled!"
