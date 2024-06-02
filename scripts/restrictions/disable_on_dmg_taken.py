import time

from .disable_hotkey_base import DisableHotkeyBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.attributes import ABILITY, SUMMONER_SPELL
from ..utils.constants import Constants


class DisableOnDmgTaken(DisableHotkeyBase):
    title = "Disable all on dmg taken!"
    difficulty = 2
    attributes = [ABILITY, SUMMONER_SPELL]

    hotkey_types = {
        Constants.ABILITY: [0, 1, 2, 3],
        Constants.SUMMONER_SPELL: [0, 1],
    }

    disable = False
    disable_end_time = 0

    @classmethod
    def init(cls):
        cls.disable = False
        cls.disable_end_time = 0
        cls.last_health_diff = cls.get_health_diff()

    @classmethod
    def restriction_content(cls):
        current_health_diff = cls.get_health_diff()

        if cls.disable:
            if time.time() < cls.disable_end_time:
                cls.disable_hotkey(True)
            else:
                cls.disable_hotkey(False)
                cls.disable = False
        elif cls.last_health_diff < current_health_diff:
            cls.disable_end_time = time.time() + 1
            cls.disable = True

        cls.last_health_diff = current_health_diff

    @classmethod
    def get_health_diff(cls):
        max_health = ActivePlayerData.get_champion_stat("maxHealth")
        current_health = ActivePlayerData.get_champion_stat("currentHealth")
        health_diff = max_health - current_health

        return health_diff
