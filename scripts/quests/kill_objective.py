from .kill_quest_base import KillQuestBase
from ..utils.constants import Constants


class KillOjective(KillQuestBase):
    title = "Kill one objective!"
    difficulty = 2
    event_names = ["DragonKill", "HordeKill", "HeraldKill", "BaronKill"]
    attributes = [Constants.OBJECTIVE]

    @classmethod
    def kill_dependencies(cls, event: dict):
        if event["KillerName"] == cls.summoner_name:
            return True
