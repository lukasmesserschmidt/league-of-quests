from random import choice

from .restriction_hotkey_base import RestrictionHotkeyBase
from ..lol_data.active_player_data import ActivePlayerData
from ..lol_data.lol_window_data import LolWindowData
from ..utils.constants import Constants
from ..utils.attributes import AUTO


class AutoLevel(RestrictionHotkeyBase):
    title = "Auto level random ability!"
    difficulty = 1
    attributes = [AUTO]

    hotkey_types = {Constants.LEVEL_ABILITY: []}

    @classmethod
    def restriction_content(cls):
        current_level = ActivePlayerData.get_level()
        total_level = cls.get_total_ability_level()
        ability_nums = [0, 1, 2, 3]

        while total_level < current_level and LolWindowData.lol_is_top and ability_nums:
            total_level = cls.get_total_ability_level()
            rand_ability = choice(ability_nums)
            ability_nums.remove(rand_ability)

            cls.hotkey_types = {Constants.LEVEL_ABILITY: [rand_ability]}
            cls.hotkey_event(Constants.PRESS_RELEASE, cls.hotkey_types)

    @classmethod
    def get_total_ability_level(cls):
        total_level = 0
        for ability in ("Q", "W", "E", "R"):
            total_level += ActivePlayerData.get_ability_level(ability)

        return total_level
