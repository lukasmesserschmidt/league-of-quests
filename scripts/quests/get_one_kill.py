from .kill_quest_base import KillQuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.attributes import KILL


class GetOneKill(KillQuestBase):
    title = "Get one kill!"
    difficulty = 1
    attributes = [KILL]

    @classmethod
    def get_kill_count(cls):
        return ActivePlayerData.get_kills()
