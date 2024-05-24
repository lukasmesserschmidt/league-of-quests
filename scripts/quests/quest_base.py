from PySide6.QtCore import QTimer
import time

from ..manager.settings_manager import SettingsManager


class QuestBase:
    title: str
    difficulty: int
    attributes: list

    duration = 0
    remaining_time = 0

    quest_loop_timer = None
    quest_complete = False
    interval = 200
    update_title = False
    finish_color_enabled = False

    # control
    @classmethod
    def check_dependencies(cls):
        return True

    @classmethod
    def start(cls):
        cls.quest_complete = False
        cls.finish_color_enabled = False

        cls.init()

        if cls.quest_loop_timer is None:
            cls.quest_loop_timer = QTimer()
            cls.quest_loop_timer.timeout.connect(cls._quest_loop)

        cls.quest_loop_timer.start(cls.interval)

    @classmethod
    def stop(cls):
        cls.quest_loop_timer.stop()
        cls.remaining_time = 0
        cls.on_end()

    # quest
    @classmethod
    def init(cls, duration_multiplier: float | int = 1):
        cls.duration = cls.get_duration(duration_multiplier)
        cls.end_time = cls.get_end_time(cls.duration)

    @classmethod
    def _quest_loop(cls):

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

    @classmethod
    def on_end(cls):
        pass

    # utils
    @classmethod
    def get_duration(cls, multiplier: float | int = 1):
        return SettingsManager.get_quest_duration() * multiplier

    @classmethod
    def get_end_time(cls, duration):
        return time.time() + duration

    @classmethod
    def get_remaining_time(cls, end_time):
        return end_time - time.time()
