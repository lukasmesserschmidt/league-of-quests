from .quest_completion_base import QuestCompletionBase

from ..lol_data.active_player_data import ActivePlayerData
from ..utils.constants import Constants


class HaveLowGold(QuestCompletionBase):
    title = "Have less than 100 gold!"
    difficulty = 0
    attributes = [Constants.GOLD]

    @classmethod
    def check_dependencies(cls):
        current_gold = ActivePlayerData.get_current_gold()
        if current_gold >= 150:
            return True

    @classmethod
    def quest_content(cls):
        current_gold = ActivePlayerData.get_current_gold()
        cls.complete = current_gold < 100
