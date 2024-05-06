from .quest_base import QuestBase


class QuestCompletionBase(QuestBase):
    completion_duration = 20
    remaining_quest_time = 0

    complete = False
    _last_complete = False
    _set_end_time = False

    @classmethod
    def init(cls):
        super().init()
        cls.remaining_quest_time = cls.duration

    @classmethod
    def quest_content_container(cls):
        cls.quest_content()

        if cls._last_complete != cls.complete:
            cls._set_end_time = True

        if cls.complete:
            if cls._set_end_time:
                cls._on_set_end_time(cls.completion_duration, True)

            cls.remaining_time = cls.get_remaining_time(cls.end_time)
        else:
            if cls._set_end_time:
                cls._on_set_end_time(cls.remaining_quest_time, False)

            cls.remaining_quest_time = cls.get_remaining_time(cls.end_time)
            cls.remaining_time = cls.remaining_quest_time

        cls._last_complete = cls.complete

    @classmethod
    def _on_set_end_time(cls, duration: float, finish_enable: bool):
        cls.end_time = cls.get_end_time(duration)
        cls.finish_color_enabled = finish_enable
        cls._set_end_time = False

    @classmethod
    def set_complete(cls, enable: bool):
        if enable:
            cls.complete = True
        else:
            cls.complete = False
