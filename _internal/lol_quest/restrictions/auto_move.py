import pyautogui

from .restriction_base import RestrictionBase
from ..lol_data.lol_window_data import LolWindowData
from ..gui.quest_display import get_quest_display


class AutoMove(RestrictionBase):
    title = "Auto move!"
    difficulty = 1

    @classmethod
    def restriction_content(cls):
        if LolWindowData.lol_is_top and not get_quest_display().dragg:
            pyautogui.rightClick()

    @classmethod
    def on_end(cls):
        if LolWindowData.lol_is_top and not get_quest_display().dragg:
            pyautogui.mouseUp(button="secondary")
