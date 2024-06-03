from random import randint
import time

from .restriction_hotkey_base import RestrictionHotkeyBase
from ..utils.attributes import MOVE
from ..utils.constants import Constants


class StopMove(RestrictionHotkeyBase):
    title = "Randomly lock movement!"
    difficulty = 0
    hotkey_type = {Constants.STOP_POSITION: [0]}
    attributes = [MOVE]

    interval = 200

    lock_move = False
    lock_end_time = 0

    @classmethod
    def init(cls):
        cls.lock_move = False
        cls.lock_end_time = 0

    @classmethod
    def restriction_content(cls):
        if cls.lock_move:
            if time.time() < cls.lock_end_time:
                cls.hotkey_event(Constants.PRESS_RELEASE, cls.hotkey_type)
            else:
                cls.lock_move = False
        elif randint(1, int(20000 / cls.interval)) == 1:
            cls.lock_end_time = time.time() + 3
            cls.lock_move = True
