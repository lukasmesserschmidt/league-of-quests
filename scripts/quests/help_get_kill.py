from random import choice

from .kill_quest_base import KillQuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.constants import Constants


class HelpGetKill(KillQuestBase):
    title = "Help teammate x get one kill!"
    difficulty = 1
    event_names = ["ChampionKill"]
    attributes = [Constants.KILL]

    @classmethod
    def check_dependencies(cls):
        return any(ActivePlayerData.get_teammates()) and any(
            ActivePlayerData.get_enemy_team()
        )

    @classmethod
    def init(cls):
        teammates = ActivePlayerData.get_teammates()
        cls.teammate_name = choice(teammates)["riotIdGameName"]
        super().init()

        cls.title = f"Help teammate {cls.teammate_name} get one kill!"

    @classmethod
    def kill_dependencies(cls, event: dict):
        if (
            event["KillerName"] == cls.teammate_name
            and cls.summoner_name in event["Assisters"]
        ):
            return True
