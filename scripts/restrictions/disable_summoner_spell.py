from random import randint

from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import SUMMONER_SPELL
from ..utils.constants import Constants


class DisableSummonerSpell(DisableHotkeyBase):
    title = "Summoner spell ? is disabled!"
    difficulty = 1
    attributes = [SUMMONER_SPELL]

    hotkey_types = {Constants.SUMMONER_SPELL: []}

    @classmethod
    def init(cls):
        super().init()
        rand_summoner_spell = randint(0, 1)
        cls.hotkey_types = {Constants.SUMMONER_SPELL: [rand_summoner_spell]}

        cls.title = f"Summoner spell {rand_summoner_spell + 1} is disabled!"
