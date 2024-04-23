import time

from .restriction_base import RestrictionBase
from ..manager.disable_manager import DisableManager
from ..lol_data.active_player_data import AcitvePlayerData


class DisableOnDmgTaken(RestrictionBase):
    title = "Disable all on dmg taken!"
    difficulty = 2
    ability_nums = [[0, 1, 2, 3], [0, 1]]
    hotkey_types = ["ability", "summoner_spell"]

    @classmethod
    def on_start(cls):
        cls.last_health_diff = cls.get_health_diff()

    @classmethod
    def restriction_content(cls):
        current_health_diff = cls.get_health_diff()

        if cls.last_health_diff < current_health_diff:
            cls.enable_type(False)
            time.sleep(0.5)
            cls.enable_type(True)

        cls.last_health_diff = current_health_diff

    @classmethod
    def on_end(cls):
        cls.enable_type(True)

    @classmethod
    def enable_type(cls, enable: bool):
        for hotkey_type, ability_num in zip(cls.hotkey_types, cls.ability_nums):
            DisableManager.enable_type(enable, hotkey_type, *ability_num)

    @classmethod
    def get_health_diff(cls):
        health_data = AcitvePlayerData.get_health_data()
        health_diff = health_data["max"] - health_data["value"]

        return health_diff
