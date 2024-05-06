from .quest_base import QuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..lol_data.event_data import EventData
from ..utils.attributes import KILL


class GetOneKill(QuestBase):
    title = "Get one kill!"
    difficulty = 1
    attributes = [KILL]

    @classmethod
    def init(cls):
        super().init()
        cls.summoner_name = ActivePlayerData.get_summoner_name()
        cls.last_kill_count = cls.get_kill_count()

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
            if event["KillerName"] == cls.summoner_name:
                kill_count += 1

        return kill_count
