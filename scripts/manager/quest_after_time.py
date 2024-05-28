from PySide6.QtCore import QTimer
import time

from .quest_frame_manager import QuestFrameManager
from .settings_manager import SettingsManager


class QuestAfterTime:
    remaining_time = 0
    receive_loop_timer = None

    @classmethod
    def start(cls):
        if cls.receive_loop_timer is None:
            cls.receive_loop_timer = QTimer()
            cls.receive_loop_timer.timeout.connect(cls.receive_loop)

        cls.cycle_time = SettingsManager.get_quest_after_time("time")
        cls.end_time = cls._get_end_time()
        cls.remaining_time = cls._get_remaining_time()

        cls.receive_loop_timer.start(500)

    @classmethod
    def stop(cls):
        if cls.receive_loop_timer is not None:
            cls.receive_loop_timer.stop()
            cls.remaining_time = 0

    @classmethod
    def receive_loop(cls):
        if cls.end_time <= time.time():
            QuestFrameManager.create_quest_frame_amount += 1
            cls.end_time = cls._get_end_time()

        cls.remaining_time = cls._get_remaining_time()

    @classmethod
    def _get_end_time(cls):
        end_time = time.time() + cls.cycle_time

        return end_time

    @classmethod
    def _get_remaining_time(cls):
        remaining_time = cls.end_time - time.time()

        return remaining_time
