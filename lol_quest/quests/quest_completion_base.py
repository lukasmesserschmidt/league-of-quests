from .quest_base import QuestBase


class QuestCompletionBase(QuestBase):
    completion_duration = 20
    remaining_quest_time = 0

    complete = None
    completing = False

    @classmethod
    def init(cls):
        super().init()
        cls.complete = False
        cls.completing = True
        cls.remaining_quest_time = cls.duration

    @classmethod
    def quest_content_container(cls):
        if cls.complete:
            if not cls.completing:
                cls._on_completing(cls.completion_duration, True)

            cls.completing = True
            cls.remaining_time = cls.get_remaining_time(cls.end_time)
        else:
            if cls.completing:
                cls._on_completing(cls.remaining_quest_time, False)

            cls.completing = False
            cls.remaining_quest_time = cls.get_remaining_time(cls.end_time)
            cls.remaining_time = cls.remaining_quest_time

        cls.quest_content()

    @classmethod
    def _on_completing(cls, duration: float, finish_enable: bool):
        cls.end_time = cls.get_end_time(duration)
        cls.finish_color_enabled = finish_enable
