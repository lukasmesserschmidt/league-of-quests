from random import randint

from .restriction_hotkey_base import RestrictionHotkeyBase
from ..utils.attributes import SUMMONER_SPELL, AUTO
from ..utils.constants import Constants


class AutoSummonerSpell(RestrictionHotkeyBase):
    title = "Auto cast random summoner spell!"
    difficulty = 1
    attributes = [SUMMONER_SPELL, AUTO]

    hotkey_types = {Constants.SUMMONER_SPELL: [], Constants.QUICK_SUMMONER_SPELL: []}

    @classmethod
    def restriction_content(cls):
        if randint(1, int(90000 / cls.interval)) == 1:
            rand_summoner_spell = randint(0, 1)
            cls.hotkey_types = {
                Constants.SUMMONER_SPELL: [rand_summoner_spell],
                Constants.QUICK_SUMMONER_SPELL: [rand_summoner_spell],
            }
            cls.hotkey_event(Constants.PRESS_RELEASE, cls.hotkey_types)
