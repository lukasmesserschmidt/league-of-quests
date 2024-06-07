from .quest_base import QuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..lol_data.score_data import ScoreData
from ..utils.constants import Constants


class GetCs(QuestBase):
    title = "Have ? cs!"
    difficulty = 0
    attributes = [Constants.CS, Constants.GET_SCORE]

    @classmethod
    def init(cls):
        super().init()
        cls.summoner_name = ActivePlayerData.get_summoner_name()
        cls.goal_cs = ScoreData.get_cs(cls.summoner_name) + 20

        cls.title = f"Have {cls.goal_cs} cs!"

    @classmethod
    def quest_content(cls):
        current_cs = ScoreData.get_cs(cls.summoner_name)

        if current_cs >= cls.goal_cs:
            cls.quest_complete = True
