from .kill_quest_base import KillQuestBase
from ..utils.constants import Constants


class AssistObjective(KillQuestBase):
    title = "Assist one objective!"
    difficulty = 1
    event_names = ["DragonKill", "HordeKill", "HeraldKill", "BaronKill"]
    attributes = [Constants.OBJECTIVE]

    @classmethod
    def kill_dependencies(cls, event: dict):
        return cls.summoner_name in event["Assisters"]
