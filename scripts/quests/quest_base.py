"""
This module contains the QuestBase class.
"""

import time

from ..common_classes.quest_restriction_base import QuestRestrictionBase
from ..manager.settings_manager import SettingsManager
from ..utils.constants import Constants


class QuestBase(QuestRestrictionBase):
    """
    The base class for all quests.
    """

    # init variables
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
        """
        Initializes the quests duration and end time.
        """
        cls.duration = cls.get_duration(max_duration)
        cls.end_time = cls.get_end_time(cls.duration)

    @classmethod
    def _update_loop(cls):
        if time.time() < cls.end_time and not cls.quest_complete:
            cls.quest_content_container()
        elif not cls.quest_complete:
            cls.on_time_end()

    @classmethod
    def quest_content_container(cls):
        """
        The content of the quest that gets updated every loop before the quest content.
        """
        cls.remaining_time = cls.get_remaining_time(cls.end_time)
        cls.quest_content()

    @classmethod
    def quest_content(cls):
        """
        The content of the quest that gets updated every loop.
        """
        raise NotImplementedError

    @classmethod
    def on_time_end(cls):
        """
        Is called when the quest times out.
        """
        cls.quest_complete = True

    # utils
    @classmethod
    def get_duration(cls, max_duration):
        """
        Returns the duration of the quest from the Settings if it is smaller than the max duration.
        """
        duration = SettingsManager.get_quest_duration()
        if duration > max_duration:
            duration = max_duration
        return duration

    @classmethod
    def get_end_time(cls, duration):
        """
        Sets the end time of the quest to the current time plus the duration and returns it.
        """
        return time.time() + duration

    @classmethod
    def get_remaining_time(cls, end_time):
        """
        Returns the remaining time of the quest.
        """
        return end_time - time.time()
