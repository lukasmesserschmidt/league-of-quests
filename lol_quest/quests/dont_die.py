from .quest_base import QuestBase

from ..lol_data.active_player_data import ActivePlayerData
from ..utils.attributes import DEATH


class DontDie(QuestBase):
    title = "Dont die or timer x3!"
    difficulty = 0
    attributes = [DEATH]

    @classmethod
    def init(cls):
        cls.finish_color_enabled = True
        cls.duration = cls.get_duration(1 / 3)
        cls.max_duration = cls.duration * 5
        cls.last_deaths = ActivePlayerData.get_deaths()

    @classmethod
    def quest_content(cls):
        current_deaths = ActivePlayerData.get_deaths()

        if cls.last_deaths < current_deaths:
            new_duration = cls.remaining_time * 3
            if new_duration >= cls.max_duration:
                new_duration = cls.max_duration

            cls.end_time = cls.get_end_time(new_duration)

        cls.last_deaths = current_deaths
