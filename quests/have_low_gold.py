from .quest_completion_base import QuestCompletionBase

from ..lol_data.active_player_data import AcitvePlayerData
from ..utils.attributes import GOLD


class HaveLowGold(QuestCompletionBase):
    title = "Have less than 100 gold!"
    difficulty = 0
    attributes = [GOLD]

    @classmethod
    def check_dependencies(cls):
        current_gold = AcitvePlayerData.get_current_gold()
        if current_gold >= 150:
            return True

        return False

    @classmethod
    def quest_content(cls):
        current_gold = AcitvePlayerData.get_current_gold()
        if current_gold < 100:
            return True
