from random import randint

from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import SUMMONER_SPELL


class DisableSummonerSpell(DisableHotkeyBase):
    title = "Summoner spell ? is disabled!"
    difficulty = 1
    attributes = [SUMMONER_SPELL]

    @classmethod
    def init(cls):
        super().init()
        rand_summoner_spell = randint(0, 1)
        cls.disable_types = {"summoner_spell": [rand_summoner_spell]}

        cls.title = f"Summoner spell {rand_summoner_spell + 1} is disabled!"
