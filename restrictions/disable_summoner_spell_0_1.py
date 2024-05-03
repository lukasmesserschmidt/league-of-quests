from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import SUMMONER_SPELL


class DisableSummonerSpell0(DisableHotkeyBase):
    title = "Summoner spell 1 is disabled!"
    difficulty = 1
    disable_types = {"summoner_spell": [0]}
    attributes = [SUMMONER_SPELL]


class DisableSummonerSpell1(DisableHotkeyBase):
    title = "Summoner spell 2 is disabled!"
    difficulty = 1
    disable_types = {"summoner_spell": [1]}
    attributes = [SUMMONER_SPELL]
