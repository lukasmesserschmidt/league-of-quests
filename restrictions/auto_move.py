import pyautogui

from .restriction_base import RestrictionBase
from ..utils.top_window_is_lol import lol_is_top


class AutoMove(RestrictionBase):
    title = "auto move click (AUTO-CLICKER!!!)!"
    difficulty = 1

    @classmethod
    def restriction_content(cls):
        if lol_is_top:
            pyautogui.rightClick()
