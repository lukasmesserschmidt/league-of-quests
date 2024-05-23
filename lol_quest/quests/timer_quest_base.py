from typing import Callable

from .quest_base import QuestBase


class TimerQuestBase(QuestBase):
    get_stat_func: Callable

    max_doubling_number = 4

    @classmethod
    def init(cls):
        super().init(1 / 12)
        cls.complete = False
        cls._doubling_number = cls.max_doubling_number
        cls.last_stat = cls.get_stat_func()

    @classmethod
    def quest_content(cls):
        current_stat = cls.get_stat_func()

        if cls.complete_condition(current_stat):
            cls.complete = True
            cls.finish_color_enabled = True

        cls.last_stat = current_stat

    @classmethod
    def on_time_end(cls):
        if cls._doubling_number > 0 and not cls.complete:
            cls.duration *= 2
            cls.end_time = cls.get_end_time(cls.duration)
            cls._doubling_number -= 1
        else:
            cls.quest_complete = True

    @classmethod
    def complete_condition(cls, current_stat):
        raise NotImplementedError
