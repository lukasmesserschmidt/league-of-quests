from random import randint

from .restriction_hotkey_base import RestrictionHotkeyBase
from ..utils.constants import Constants


class AutoRecall(RestrictionHotkeyBase):
    title = "Randomly auto cast recall!"
    difficulty = 0
    attributes = [Constants.RECALL, Constants.AUTO]

    hotkey_types = {Constants.RECALL: [0]}

    @classmethod
    def restriction_content(cls):
        if randint(1, int(20000 / cls.interval)) == 1:
            cls.hotkey_event(Constants.PRESS_RELEASE, cls.hotkey_types)
