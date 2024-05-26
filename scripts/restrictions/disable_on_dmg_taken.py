import time

from .disable_hotkey_base import DisableHotkeyBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.attributes import ABILITY, SUMMONER_SPELL


class DisableOnDmgTaken(DisableHotkeyBase):
    title = "Disable all on dmg taken!"
    difficulty = 2
    disable_hotkeys = {"ability": [0, 1, 2, 3], "summoner_spell": [0, 1]}
    attributes = [ABILITY, SUMMONER_SPELL]

    disable = False
    disable_end_time = 0

    @classmethod
    def init(cls):
        super().init()
        cls.disable = False
        cls.disable_end_time = 0
        cls.last_health_diff = cls.get_health_diff()

    @classmethod
    def restriction_content(cls):
        current_health_diff = cls.get_health_diff()

        if cls.disable:
            if time.time() < cls.disable_end_time:
                cls.enable_hotkey(False)
            else:
                cls.enable_hotkey(True)
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
