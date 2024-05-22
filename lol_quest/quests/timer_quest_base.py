from typing import Callable

from .quest_base import QuestBase


class TimerQuestBase(QuestBase):
    get_stat_func: Callable

    @classmethod
    def init(cls):
        cls.duration = cls.get_duration(1 / 12)
        cls.complete = False
        cls.last_stat = cls.get_stat_func()

    @classmethod
    def quest_loop_container(cls):
        for _ in range(4):
            cls._quest_loop()

            cls.duration *= 2

            if cls.complete:
                break

    @classmethod
    def quest_content(cls):
        current_stat = cls.get_stat_func()

        if cls.complete_condition(current_stat):
            cls.complete = True
            cls.finish_color_enabled = True

        cls.last_stat = current_stat

    @classmethod
    def complete_condition(cls, current_stat):
        raise NotImplementedError
