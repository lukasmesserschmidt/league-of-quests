from random import choice

from .kill_quest_base import KillQuestBase
from ..utils.attributes import KILL
from ..lol_data.active_player_data import ActivePlayerData


class StealKill(KillQuestBase):
    title = "Steal teammate x one kill!"
    difficulty = 2
    event_names = ["ChampionKill"]
    attributes = [KILL]

    @classmethod
    def check_dependencies(cls):
        return any(ActivePlayerData.get_teammates())

    @classmethod
    def init(cls):
        teammates = ActivePlayerData.get_teammates()
        cls.teammate_name = choice(teammates)["riotIdGameName"]
        super().init()

        cls.title = f"Steal teammate {cls.teammate_name} one kill!"

    @classmethod
    def kill_dependencies(cls, event: dict):
        if (
            event["KillerName"] == cls.summoner_name
            and cls.teammate_name in event["Assisters"]
        ):
            return True
