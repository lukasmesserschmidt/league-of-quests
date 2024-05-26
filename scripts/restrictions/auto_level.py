from random import choice

from .restriction_base import RestrictionBase
from ..lol_data.active_player_data import ActivePlayerData
from ..manager.hotkey_manager import HotkeyManager
from ..lol_data.lol_window_data import LolWindowData
from ..utils.attributes import AUTO


class AutoLevel(RestrictionBase):
    title = "Auto level random ability!"
    difficulty = 1
    attributes = [AUTO]

    @classmethod
    def restriction_content(cls):
        current_level = ActivePlayerData.get_level()
        total_level = cls.get_total_ability_level()
        ability_nums = [0, 1, 2, 3]

        while total_level < current_level and LolWindowData.lol_is_top and ability_nums:
            total_level = cls.get_total_ability_level()
            rand_ability = choice(ability_nums)
            ability_nums.remove(rand_ability)

            hotkey_type = {"level_ability": [rand_ability]}
            HotkeyManager().hotkey_event("press_release", hotkey_type)

    @classmethod
    def get_total_ability_level(cls):
        total_level = 0
        for ability in ("Q", "W", "E", "R"):
            total_level += ActivePlayerData.get_ability_level(ability)

        return total_level
