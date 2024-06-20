import time

from .cycle_base import CycleBase
from .restriction_hotkey_base import RestrictionHotkeyBase
from ..utils.constants import Constants


class AutoAllAbilities(CycleBase, RestrictionHotkeyBase):
    title = "Auto cast all abilities!"
    difficulty = 2
    attributes = [Constants.ABILITY, Constants.AUTO]

    hotkey_types = {
        Constants.ABILITY: [0, 1, 2, 3],
        Constants.QUICK_ABILITY: [0, 1, 2, 3],
    }

    cycle_duration = 2
    start_end_time = 0

    @classmethod
    def init(cls):
        super().init()
        cls.start_end_time = time.time() + 10

    @classmethod
    def start_condition(cls):
        return cls.start_end_time < time.time()

    @classmethod
    def cycle_content(cls):
        cls.hotkey_event(Constants.PRESS_RELEASE, cls.hotkey_types)

    @classmethod
    def cycle_end(cls):
        cls.start_end_time = time.time() + 40
