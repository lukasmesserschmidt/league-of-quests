"""
This module contains the QuestFrameManager class.
"""

from PySide6.QtCore import QTimer

from .quest_frame_creator import QuestFrameCreator
from .settings_manager import SettingsManager
from ..gui.quest_frame import QuestFrame
from ..gui.quest_display import QuestDisplay


class QuestFrameManager:
    """
    A class for managing the quest frames.
    """

    # init variables
    active_quest_frames = []

    create_quest_frame_amount = 0
    quest_frames_available = True
    _update_loop_timer = None

    @classmethod
    def start(cls):
        """
        Start the update loop timer, reset the create quest frame amount and active quest frames.
        """
        if cls._update_loop_timer is None:
            cls._update_loop_timer = QTimer()
            cls._update_loop_timer.timeout.connect(cls._update_loop)

        cls.active_quest_frames = []
        cls.create_quest_frame_amount = 0
        cls._update_loop_timer.start(500)

    @classmethod
    def stop(cls):
        """
        Stop the update loop timer, reset the create quest frame amount and delete all active quest frames.
        """
        if cls._update_loop_timer is not None:
            cls._update_loop_timer.stop()
            cls.create_quest_frame_amount = 0

            for i in range(len(cls.active_quest_frames) - 1, -1, -1):
                quest_frame = cls.active_quest_frames[i]
                cls._delete_quest_frame(quest_frame)

    @classmethod
    def _update_loop(cls):
        for _ in range(cls.create_quest_frame_amount):
            if len(cls.active_quest_frames) < SettingsManager.get_quest_limit():
                cls._create_quest_frame()
            cls.create_quest_frame_amount -= 1

        cls._update_quest_frames()
        cls._update_quest_frame_available()

    @classmethod
    def _create_quest_frame(cls):
        quest_frame = QuestFrameCreator.get_quest_frame(cls.active_quest_frames)
        if quest_frame:
            QuestDisplay.get_instance().add_widget(quest_frame)
            cls.active_quest_frames.append(quest_frame)

    @classmethod
    def _update_quest_frames(cls):
        for quest_frame in cls.active_quest_frames:
            quest = quest_frame.quest
            if quest.quest_complete:
                cls._delete_quest_frame(quest_frame)

    @classmethod
    def _delete_quest_frame(cls, quest_frame: QuestFrame):
        quest_frame.restriction.stop()
        quest_frame.quest.stop()
        cls.active_quest_frames.remove(quest_frame)
        quest_frame.deleteLater()

    @classmethod
    def _update_quest_frame_available(cls):
        objects = QuestFrameCreator.get_compatible(cls.active_quest_frames)

        if objects:
            cls.quest_frames_available = True
        else:
            cls.quest_frames_available = False
