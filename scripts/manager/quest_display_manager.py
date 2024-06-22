"""
This module contains the QuestDisplayManager class.
"""

from PySide6.QtCore import QTimer

from .quest_frame_manager import QuestFrameManager
from .quest_after_time import QuestAfterTime
from .settings_manager import SettingsManager
from ..gui.quest_display import QuestDisplay
from ..utils.time import convert_time


class QuestDisplayManager:
    """
    A class for managing the quest display.
    """

    # init variables
    _update_loop_timer = None
    _quest_display = QuestDisplay.get_instance()

    @classmethod
    def start(cls):
        """
        Start the update loop timer.
        """
        if cls._update_loop_timer is None:
            cls._update_loop_timer = QTimer()
            cls._update_loop_timer.timeout.connect(cls._update_loop)

        cls._update_loop_timer.start(500)

    @classmethod
    def stop(cls):
        """
        Stop the update loop timer.
        """
        if cls._update_loop_timer is not None:
            cls._update_loop_timer.stop()
            cls._quest_display.set_timer_text("00:00")

    @classmethod
    def _update_loop(cls):
        cls._update_timer_text()
        cls._update_quest_count()

    @classmethod
    def _update_timer_text(cls):
        if not QuestFrameManager.quest_frames_available:
            if cls._quest_display.get_timer_text() != "N/A":
                cls._quest_display.set_timer_text("N/A")
        elif (
            len(QuestFrameManager.active_quest_frames)
            < SettingsManager.get_quest_limit()
        ):
            if SettingsManager.get_quest_after_time():
                cls._quest_display.set_timer_text(
                    convert_time(QuestAfterTime.remaining_time)
                )
            elif cls._quest_display.get_timer_text() != "Not Active":
                cls._quest_display.set_timer_text("Not Active")

        elif cls._quest_display.get_timer_text() != "Max Quests":
            cls._quest_display.set_timer_text("Max Quests")

    @classmethod
    def _update_quest_count(cls):
        quest_count = len(QuestFrameManager.active_quest_frames)
        if cls._quest_display.get_quest_count() != str(quest_count):
            cls._quest_display.set_quest_count(quest_count)
