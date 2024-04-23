import pyautogui

from .restriction_base import RestrictionBase
from ..utils.top_window_is_lol import get_top_window_is_lol


class AutoMove(RestrictionBase):
    title = "auto move click (AUTO-CLICKER!!!)!"
    difficulty = 1

    @classmethod
    def restriction_content(cls):
        if get_top_window_is_lol():
            pyautogui.rightClick()
