from random import randint

from .restriction_hotkey_base import RestrictionHotkeyBase
from ..utils.constants import Constants
from ..utils.attributes import TRINKET, AUTO
from ..utils.constants import Constants


class AutoTrinket(RestrictionHotkeyBase):
    title = "Randomly auto cast trinket!"
    difficulty = 1
    attributes = [TRINKET, AUTO]

    hotkey_types = {Constants.TRINKET: [0], Constants.QUICK_TRINKET: [0]}

    @classmethod
    def restriction_content(cls):
        if randint(1, int(40000 / cls.interval)) == 1:
            cls.hotkey_event(Constants.PRESS_RELEASE, cls.hotkey_types)
