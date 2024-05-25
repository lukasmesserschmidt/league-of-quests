import pyautogui

from .restriction_thread_base import RestrictionThreadBase
from ..lol_data.lol_window_data import LolWindowData
from ..gui.quest_display import get_quest_display
from ..utils.is_game_active import is_game_active
from ..utils.attributes import MOVE, AUTO


class AutoMove(RestrictionThreadBase):
    title = "Auto move!"
    difficulty = 1
    attributes = [MOVE, AUTO]

    interval = 0.1

    @classmethod
    def stop(cls):
        super().stop()
        pyautogui.FAILSAFE = True

    @classmethod
    def init(cls):
        pyautogui.FAILSAFE = False

    @classmethod
    def restriction_content(cls):
        if (
            LolWindowData.lol_is_top
            and is_game_active()
            and not get_quest_display().dragg
        ):
            LolWindowData.activate_lol()
            pyautogui.rightClick()

    @classmethod
    def on_end(cls):
        if (
            LolWindowData.lol_is_top
            and is_game_active()
            and not get_quest_display().dragg
        ):
            LolWindowData.activate_lol()
            pyautogui.mouseUp(button="secondary")
