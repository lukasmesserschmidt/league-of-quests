from random import randint

from .quest_base import QuestBase
from ..lol_data.active_player_data import AcitvePlayerData
from ..lol_data.all_player_data import AllPlayerDate
from ..lol_data.event_data import EventData
from ..utils.attributes import KILL


class SoloKill(QuestBase):
    title = "Solo kill player x!"
    difficulty = 2
    attributes = [KILL]

    @classmethod
    def check_dependencies(cls):
        return cls.get_target()

    @classmethod
    def init(cls):
        super().init()
        cls.target = cls.get_target()
        cls.title = f"Solo kill {cls.target["championName"]} ({cls.target["summonerName"]})!"
        cls.summoner_name = AcitvePlayerData.get_summoner_name()
        cls.last_kill_count = cls.get_kill_count()

    @classmethod
    def quest_content(cls):
        if cls.last_kill_count < cls.get_kill_count():
            cls.terminate_flag = True
        
    @classmethod
    def get_target(cls):
        enemy_team_num = AcitvePlayerData.get_team() - 1
        enemy_team = AllPlayerDate.get_team_players()[enemy_team_num]
        if any(enemy_team):
            rand_target = randint(0, len(enemy_team) - 1)
            target = enemy_team[rand_target]
            return target

        return False
    
    @classmethod
    def get_kill_count(cls):
        kill_events = EventData.get_kill_events()
        kill_count = 0

        for event in kill_events:
            if (
                event["Assisters"] == []
                and event["KillerName"] == cls.summoner_name
                and event["VictimName"] == cls.target["summonerName"]
            ):
                kill_count += 1
        
        return kill_count
