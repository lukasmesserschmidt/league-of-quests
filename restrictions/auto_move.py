import pyautogui

from .restriction_base import RestrictionBase
from ..lol_data.lol_window_data import LolWindowData


class AutoMove(RestrictionBase):
    title = "auto move click (AUTO-CLICKER!!!)!"
    difficulty = 1

    @classmethod
    def restriction_content(cls):
        if LolWindowData.lol_is_top:
            pyautogui.rightClick()
