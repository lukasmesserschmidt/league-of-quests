from random import randint

from .restriction_disable_hotkey_base import RestrictionDisableHotkeyBase
from ..utils.constants import Constants


class DisableSummonerSpell(RestrictionDisableHotkeyBase):
    title = "Summoner spell ? is disabled!"
    difficulty = 1
    attributes = [Constants.SUMMONER_SPELL]

    hotkey_types = {Constants.SUMMONER_SPELL: []}

    @classmethod
    def init(cls):
        super().init()
        rand_summoner_spell = randint(0, 1)
        cls.set_hotkey_types((Constants.SUMMONER_SPELL, [rand_summoner_spell]))

        cls.title = f"Summoner spell {rand_summoner_spell + 1} is disabled!"
