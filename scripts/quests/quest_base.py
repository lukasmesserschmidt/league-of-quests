import time

from ..common_classes.quest_restriction_base import QuestRestrictionBase
from ..manager.settings_manager import SettingsManager
from ..utils.constants import Constants


class QuestBase(QuestRestrictionBase):
    duration = 0
    remaining_time = 0

    quest_complete = False

    update_title = False
    finish_color_enabled = False

    # control
    @classmethod
    def start(cls):
        cls.quest_complete = False
        cls.finish_color_enabled = False

        super().start()

    @classmethod
    def stop(cls):
        cls.main_loop_timer.stop()
        cls.remaining_time = 0
        cls.on_end()

    # quest
    @classmethod
    def init(cls, max_duration: int = Constants.MAX_DURATION):
        cls.duration = cls.get_duration(max_duration)
        cls.end_time = cls.get_end_time(cls.duration)

    @classmethod
    def _main_loop(cls):
        if time.time() < cls.end_time and not cls.quest_complete:
            cls.quest_content_container()
        elif not cls.quest_complete:
            cls.on_time_end()

    @classmethod
    def quest_content_container(cls):
        cls.remaining_time = cls.get_remaining_time(cls.end_time)
        cls.quest_content()

    @classmethod
    def quest_content(cls):
        raise NotImplementedError

    @classmethod
    def on_time_end(cls):
        cls.quest_complete = True

    # utils
    @classmethod
    def get_duration(cls, max_duration):
        duration = SettingsManager.get_quest_duration()
        if duration > max_duration:
            duration = max_duration
        return duration

    @classmethod
    def get_end_time(cls, duration):
        return time.time() + duration

    @classmethod
    def get_remaining_time(cls, end_time):
        return end_time - time.time()
