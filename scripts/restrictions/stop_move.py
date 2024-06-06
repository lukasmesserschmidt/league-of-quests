from random import randint

from .cycle_base import CycleBase
from .restriction_hotkey_base import RestrictionHotkeyBase
from ..utils.attributes import MOVE
from ..utils.constants import Constants


class StopMove(CycleBase, RestrictionHotkeyBase):
    title = "Randomly lock movement!"
    difficulty = 0
    hotkey_type = {Constants.STOP_POSITION: [0]}
    attributes = [MOVE]

    cycle_duration = 3

    @classmethod
    def start_condition(cls):
        return randint(1, int(20000 / cls.interval)) == 1

    @classmethod
    def cycle_content(cls):
        cls.hotkey_event(Constants.PRESS_RELEASE, cls.hotkey_type)
