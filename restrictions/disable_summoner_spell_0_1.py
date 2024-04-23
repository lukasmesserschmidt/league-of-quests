from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import SUMMONER_SPELL0, SUMMONER_SPELL1


class DisableSummonerSpell0(DisableHotkeyBase):
    title = "Summoner spell 1 is disabled!"
    difficulty = 1
    ability_num = [0]
    hotkey_type = "summoner_spell"
    attributes = [SUMMONER_SPELL0]


class DisableSummonerSpell1(DisableHotkeyBase):
    title = "Summoner spell 2 is disabled!"
    difficulty = 1
    ability_num = [1]
    hotkey_type = "summoner_spell"
    attributes = [SUMMONER_SPELL1]
