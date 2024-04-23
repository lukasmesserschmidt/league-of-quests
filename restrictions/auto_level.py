from random import randint
import keyboard

from .restriction_base import RestrictionBase
from ..lol_data.active_player_data import AcitvePlayerData
from ..lol_data.lol_settings import LolSettings
from ..utils.top_window_is_lol import get_top_window_is_lol


class AutoLevel(RestrictionBase):
    title = "Auto level random ability!"
    difficulty = 1

    @classmethod
    def on_start(cls):
        cls.last_level = AcitvePlayerData.get_level()

    @classmethod
    def restriction_content(cls):
        current_level = AcitvePlayerData.get_level()

        # if cls.last_level < current_level:
        total_level = cls.get_total_ability_level()
        while total_level < current_level:
            if get_top_window_is_lol():
                total_level = cls.get_total_ability_level()
                rand_hotkey = randint(0, 3)
                hotkey = LolSettings.get_level_ability_hotkey(rand_hotkey)
                keyboard.press_and_release(hotkey)
                keyboard.unhook_all()

        cls.last_level = current_level

    @classmethod
    def get_total_ability_level(cls):
        ability_level = AcitvePlayerData.get_ability_level()
        total_level = 0

        for level in ability_level.values():
            total_level += level

        return total_level
