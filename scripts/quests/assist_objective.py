from .kill_quest_base import KillQuestBase
from ..utils.attributes import OBJECTIVE


class AssistObjective(KillQuestBase):
    title = "Assist one objective!"
    difficulty = 1
    event_names = ["DragonKill", "HordeKill", "HeraldKill", "BaronKill"]
    attributes = [OBJECTIVE]

    @classmethod
    def kill_dependencies(cls, event: dict):
        return cls.summoner_name in event["Assisters"]
