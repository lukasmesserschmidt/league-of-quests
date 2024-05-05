from random import choice

from .quest_base import QuestBase
from ..utils.attributes import KILL
from ..lol_data.active_player_data import ActivePlayerData
from ..lol_data.all_player_data import AllPlayerData
from ..lol_data.event_data import EventData


class HelpGetKill(QuestBase):
    title = "Help teammate x get one kill!"
    difficulty = 1
    attributes = [KILL]

    @classmethod
    def check_dependencies(cls):
        return any(ActivePlayerData.get_teammates()) and any(
            ActivePlayerData.get_enemy_team()
        )

    @classmethod
    def init(cls):
        super().init()
        teammates = ActivePlayerData.get_teammates()
        cls.teammate_name = choice(teammates)["summonerName"]
        cls.summoner_name = ActivePlayerData.get_summoner_name()

        cls.last_kill_count = cls.get_kill_count()

        cls.title = f"Help teammate {cls.teammate_name} get one kill!"

    @classmethod
    def quest_content(cls):
        current_kill_count = cls.get_kill_count()

        if cls.last_kill_count < current_kill_count:
            cls.terminate_flag = True

    @classmethod
    def get_kill_count(cls):
        kill_events = EventData.get_event("ChampionKill")
        kill_count = 0

        for event in kill_events:
            if (
                event["KillerName"] == cls.teammate_name
                and cls.summoner_name in event["Assisters"]
            ):
                kill_count += 1

        return kill_count
