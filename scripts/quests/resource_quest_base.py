"""
This module contains the ResourceQuestBase class.
"""

from .quest_base import QuestBase
from ..common_classes.resource_base import ResouceBase


class ResourceQuestBase(ResouceBase, QuestBase):
    """
    The base class for all resource quests.
    """

    @classmethod
    def init(cls):
        super().init(40)
        cls.finish_color_enabled = True
        cls.last_resource_diff = cls.get_resource_diff()

    @classmethod
    def quest_content(cls):
        current_resource_diff = cls.get_resource_diff()

        if cls.last_resource_diff < current_resource_diff:
            cls.last_resource_diff = current_resource_diff

            cls.end_time = cls.get_end_time(cls.duration)

        cls.last_resource_diff = current_resource_diff
