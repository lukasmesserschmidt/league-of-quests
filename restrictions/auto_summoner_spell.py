from random import randint

from .restriction_base import RestrictionBase
from ..manager.hotkey_manager import HotkeyManager


class AutoSummonerSpell(RestrictionBase):
    title = "Auto cast random summoner spell!"
    difficulty = 2

    @classmethod
    def restriction_content(cls):
        if randint(1, 450) == 1:
            rand_summoner_spell = randint(0, 1)
            hotkey_type = {"quick_summoner_spell": [rand_summoner_spell]}
            HotkeyManager().set_hotkeys("press_release", hotkey_type)
            hotkey_type = {"summoner_spell": [rand_summoner_spell]}
            HotkeyManager().set_hotkeys("press_release", hotkey_type)
