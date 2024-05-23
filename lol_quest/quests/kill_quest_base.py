from .quest_base import QuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..lol_data.event_data import EventData


class KillQuestBase(QuestBase):
    event_names: list[str]

    @classmethod
    def init(cls):
        super().init()
        cls.summoner_name = ActivePlayerData.get_summoner_name()
        cls.last_kill_count = cls.get_kill_count()

    @classmethod
    def quest_content(cls):
        current_kill_count = cls.get_kill_count()

        if cls.last_kill_count < current_kill_count:
            cls.quest_complete = True

    @classmethod
    def get_kill_count(cls):
        kill_count = 0

        for event_name in cls.event_names:
            events = EventData.get_event(event_name)

            for event in events:
                if cls.kill_dependencies(event):
                    kill_count += 1

        return kill_count

    @classmethod
    def kill_dependencies(cls, event: dict):
        raise NotImplementedError
