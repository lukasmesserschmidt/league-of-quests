from .quest_completion_base import QuestCompletionBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.constants import Constants


class HaveXGold(QuestCompletionBase):
    title = "Have 3000 gold!"
    difficulty = 2
    attributes = [Constants.GOLD]

    @classmethod
    def check_dependencies(cls):
        if 1000 < ActivePlayerData.get_current_gold() < 2500:
            return True

    @classmethod
    def quest_content(cls):
        cls.complete = ActivePlayerData.get_current_gold() >= 3000
