from random import randint
import time

from .restriction_thread_base import RestrictionThreadBase
from ..manager.hotkey_manager import HotkeyManager, EventType
from ..utils.attributes import MOVE


class StopMove(RestrictionThreadBase):
    title = "Randomly lock movement!"
    difficulty = 0
    hotkey_type = {"stop_position": [0]}
    attributes = [MOVE]

    interval = 0.1

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
                HotkeyManager().hotkey_event(EventType.PRESS_RELEASE, cls.hotkey_type)
            else:
                cls.lock_move = False
        elif randint(1, int(20 / cls.interval)) == 1:
            cls.lock_end_time = time.time() + 3
            cls.lock_move = True
