from .quest_base import QuestBase

from ..lol_data.active_player_data import ActivePlayerData
from ..lol_data.score_data import ScoreData
from ..utils.constants import Constants


class GetWardScore(QuestBase):
    title = "Get ? ward score!"
    difficulty = 0
    attributes = [Constants.WARD_SCORE, Constants.TRINKET, Constants.GET_SCORE]

    update_title = True

    @classmethod
    def init(cls):
        super().init()
        cls.summoner_name = ActivePlayerData.get_summoner_name()
        cls.start_ward_score = ScoreData.get_ward_score(cls.summoner_name)

        cls.set_title(0)

    @classmethod
    def quest_content(cls):
        current_ward_score = ScoreData.get_ward_score(cls.summoner_name)
        progress = current_ward_score - cls.start_ward_score

        cls.set_title(progress)

        if progress >= 3:
            cls.quest_complete = True

    @classmethod
    def set_title(cls, progress: float):
        cls.title = f"Get {int(progress)}/3 ward score!"
