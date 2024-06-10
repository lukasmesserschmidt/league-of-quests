from .quest_base import QuestBase

from ..lol_data.active_player_data import ActivePlayerData
from ..utils.constants import Constants


class DontDie(QuestBase):
    title = "Dont die or timer x4!"
    difficulty = 0
    attributes = [Constants.DEATH, Constants.TIMER]

    @classmethod
    def init(cls):
        super().init(60)
        cls.finish_color_enabled = True
        cls.max_duration = cls.duration * 10
        cls.last_deaths = ActivePlayerData.get_deaths()

    @classmethod
    def quest_content(cls):
        current_deaths = ActivePlayerData.get_deaths()

        if cls.last_deaths < current_deaths:
            new_duration = cls.remaining_time * 4
            if new_duration >= cls.max_duration:
                new_duration = cls.max_duration

            cls.end_time = cls.get_end_time(new_duration)

        cls.last_deaths = current_deaths
