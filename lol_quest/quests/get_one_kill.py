from .kill_quest_base import KillQuestBase
from ..utils.attributes import KILL


class GetOneKill(KillQuestBase):
    title = "Get one kill!"
    difficulty = 1
    event_names = ["ChampionKill"]
    attributes = [KILL]

    @classmethod
    def kill_dependencies(cls, event: dict):
        if event["KillerName"] == cls.summoner_name:
            return True
