"""
This module contains the RestrictionBase class.
"""

from ..common_classes.quest_restriction_base import QuestRestrictionBase


class RestrictionBase(QuestRestrictionBase):
    """
    A base class for all restrictions.
    """

    # restriction
    @classmethod
    def _update_loop(cls):
        cls.restriction_content()

    @classmethod
    def restriction_content(cls):
        """
        The content of the restriction that gets updated every loop.
        """
        raise NotImplementedError
