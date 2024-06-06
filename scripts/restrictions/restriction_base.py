from ..common_classes.quest_restriction_base import QuestRestrictionBase


class RestrictionBase(QuestRestrictionBase):

    # restriction
    @classmethod
    def _main_loop(cls):
        cls.restriction_content()

    @classmethod
    def restriction_content(cls):
        raise NotImplementedError
