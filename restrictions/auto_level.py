from random import choice
import keyboard

from .restriction_base import RestrictionBase
from ..lol_data.active_player_data import AcitvePlayerData
from ..lol_data.lol_settings import LolSettings
from ..lol_data.lol_window_data import LolWindowData


class AutoLevel(RestrictionBase):
    title = "Auto level random ability!"
    difficulty = 1

    @classmethod
    def restriction_content(cls):
        current_level = AcitvePlayerData.get_level()
        total_level = cls.get_total_ability_level()
        hotkey_nums = [0, 1, 2, 3]

        while total_level < current_level and LolWindowData.lol_is_top and hotkey_nums:
            total_level = cls.get_total_ability_level()
            rand_hotkey_num = choice(hotkey_nums)
            hotkey_nums.remove(rand_hotkey_num)

            hotkey = LolSettings.get_level_ability_hotkey(rand_hotkey_num)
            keyboard.press_and_release(hotkey)
            keyboard.unhook_all()

    @classmethod
    def get_total_ability_level(cls):
        total_level = 0
        for ability in ("Q", "W", "E", "R"):
            total_level += AcitvePlayerData.get_ability_level(ability)

        return total_level
