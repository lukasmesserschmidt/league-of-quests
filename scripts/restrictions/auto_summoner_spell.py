from random import randint

from .restriction_base import RestrictionBase
from ..manager.hotkey_manager import HotkeyManager
from ..utils.attributes import SUMMONER_SPELL, AUTO


class AutoSummonerSpell(RestrictionBase):
    title = "Auto cast random summoner spell!"
    difficulty = 1
    attributes = [SUMMONER_SPELL, AUTO]

    @classmethod
    def restriction_content(cls):
        if randint(1, 450) == 1:
            rand_summoner_spell = randint(0, 1)
            hotkey_type = {"quick_summoner_spell": [rand_summoner_spell]}
            HotkeyManager().hotkey_event("press_release", hotkey_type)
            hotkey_type = {"summoner_spell": [rand_summoner_spell]}
            HotkeyManager().hotkey_event("press_release", hotkey_type)
