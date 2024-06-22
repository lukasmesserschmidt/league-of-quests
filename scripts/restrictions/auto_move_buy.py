from pynput.mouse import Controller, Button

from .restriction_base import RestrictionBase
from ..lol_data.lol_window_data import LolWindowData
from ..gui.quest_display import QuestDisplay
from ..utils.is_game_active import is_game_active
from ..utils.constants import Constants


class AutoMoveBuy(RestrictionBase):
    title = "Auto move/buy!"
    difficulty = 2
    attributes = [Constants.MOVE, Constants.AUTO]

    mouse = Controller()

    @classmethod
    def restriction_content(cls):
        if (
            LolWindowData.lol_is_top
            and is_game_active()
            and not QuestDisplay.get_instance().is_dragging
        ):
            cls.mouse.click(Button.right)
