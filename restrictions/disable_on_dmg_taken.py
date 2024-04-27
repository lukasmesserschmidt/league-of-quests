import time

from .disable_hotkey_base import DisableHotkeyBase
from ..lol_data.active_player_data import AcitvePlayerData
from ..utils.attributes import (
    ABILITY0,
    ABILITY1,
    ABILITY2,
    ABILITY3,
    SUMMONER_SPELL0,
    SUMMONER_SPELL1,
)


class DisableOnDmgTaken(DisableHotkeyBase):
    title = "Disable all on dmg taken!"
    difficulty = 2
    disable_hotkeys = {"ability": [0, 1, 2, 3], "summoner_spell": [0, 1]}
    attributes = [
        ABILITY0,
        ABILITY1,
        ABILITY2,
        ABILITY3,
        SUMMONER_SPELL0,
        SUMMONER_SPELL1,
    ]

    @classmethod
    def init(cls):
        super().init()
        cls.last_health_diff = cls.get_health_diff()

    @classmethod
    def restriction_content(cls):
        current_health_diff = cls.get_health_diff()

        if cls.last_health_diff < current_health_diff:
            cls.enable_type(False)
            time.sleep(1)
            cls.enable_type(True)

        cls.last_health_diff = current_health_diff

    @classmethod
    def get_health_diff(cls):
        health_data = AcitvePlayerData.get_health_data()
        health_diff = health_data["max"] - health_data["value"]

        return health_diff
