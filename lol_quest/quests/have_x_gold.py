from .quest_completion_base import QuestCompletionBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.attributes import GOLD


class HaveXGold(QuestCompletionBase):
    title = "Have 4000 gold!"
    difficulty = 2
    attributes = [GOLD]

    @classmethod
    def check_dependencies(cls):
        if ActivePlayerData.get_current_gold() < 2000:
            return True

    @classmethod
    def quest_content(cls):
        cls.complete = ActivePlayerData.get_current_gold() >= 4000
