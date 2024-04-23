from .quest_base import QuestBase
from ..lol_data.active_player_data import AcitvePlayerData
from ..lol_data.score_data import ScoreData
from ..utils.attributes import CS


class GetCs(QuestBase):
    title = "Have ? cs!"
    difficulty = 0
    attributes = [CS]

    @classmethod
    def on_start(cls):
        cls.summoner_name = AcitvePlayerData.get_summoner_name()
        cls.goal_cs = ScoreData.get_cs(cls.summoner_name) + 20
        cls.title = f"Have {cls.goal_cs} cs!"

    @classmethod
    def quest_content(cls):
        cs = ScoreData.get_cs(cls.summoner_name)

        if cs >= cls.goal_cs:
            return True

        return False
