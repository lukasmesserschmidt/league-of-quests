from random import randint

from .kill_quest_base import KillQuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.attributes import KILL


class SoloKill(KillQuestBase):
    title = "Solo kill player x!"
    difficulty = 2
    event_names = ["ChampionKill"]
    attributes = [KILL]

    @classmethod
    def check_dependencies(cls):
        return any(ActivePlayerData.get_enemy_team())

    @classmethod
    def init(cls):
        enemy_team = ActivePlayerData.get_enemy_team()
        rand_target = randint(0, len(enemy_team) - 1)
        cls.target = enemy_team[rand_target]
        super().init()
        
        cls.title = f"Solo kill {cls.target["championName"]} ({cls.target["summonerName"]})!"

    @classmethod
    def kill_dependencies(cls, event: dict):
        if (
            event["Assisters"] == []
            and event["KillerName"] == cls.summoner_name
            and event["VictimName"] == cls.target["summonerName"]
        ):
            return True
