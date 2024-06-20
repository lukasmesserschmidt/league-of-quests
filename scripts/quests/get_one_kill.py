from .kill_quest_base import KillQuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.constants import Constants


class GetOneKill(KillQuestBase):
    title = "Get one kill!"
    difficulty = 1
    attributes = [Constants.KILL]

    @classmethod
    def check_dependencies(cls):
        return any(ActivePlayerData.get_enemy_team())

    @classmethod
    def get_kill_count(cls):
        return ActivePlayerData.get_kills()
