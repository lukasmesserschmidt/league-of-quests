"""
This module contains the QuestAfterTime class.
"""

import time

from PySide6.QtCore import QTimer

from .quest_frame_manager import QuestFrameManager
from .settings_manager import SettingsManager


class QuestAfterTime:
    """
    A class for managing the quest after time option.
    """

    # init variables
    remaining_time = 0
    receive_loop_timer = None

    @classmethod
    def start(cls):
        """
        Start the receive loop timer.
        """
        if cls.receive_loop_timer is None:
            cls.receive_loop_timer = QTimer()
            cls.receive_loop_timer.timeout.connect(cls._receive_loop)

        cls.cycle_time = SettingsManager.get_quest_after_time_duration()
        cls.end_time = cls._get_end_time()
        cls.remaining_time = cls._get_remaining_time()

        cls.receive_loop_timer.start(500)

    @classmethod
    def stop(cls):
        """
        Stop the receive loop timer.
        """
        if cls.receive_loop_timer is not None:
            cls.receive_loop_timer.stop()
            cls.remaining_time = 0

    @classmethod
    def _receive_loop(cls):
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
