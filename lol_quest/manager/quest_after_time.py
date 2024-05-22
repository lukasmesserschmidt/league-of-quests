from PySide6.QtCore import QTimer
import time

from .quest_frame_manager import QuestFrameManager
from .settings_manager import SettingsManager


class QuestAfterTime:
    receive_loop_timer = None

    @classmethod
    def start(cls):
        if cls.receive_loop_timer is None:
            cls.receive_loop_timer = QTimer()
            cls.receive_loop_timer.timeout.connect(cls.receive_loop)

        cls.time = SettingsManager.get_quest_after_time("time")
        cls.end_time = time.time() + cls.time

        cls.receive_loop_timer.start(200)

    @classmethod
    def stop(cls):
        if cls.receive_loop_timer is not None:
            cls.receive_loop_timer.stop()
            cls.remaining_time = 0

    @classmethod
    def receive_loop(cls):
        if cls.end_time <= time.time():
            QuestFrameManager.create_quest_frame_amount += 1
            cls.end_time = time.time() + cls.time

        cls.remaining_time = cls.end_time - time.time()
