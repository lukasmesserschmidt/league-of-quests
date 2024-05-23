from random import randint
import time

from .restriction_base import RestrictionBase
from ..manager.hotkey_manager import HotkeyManager
from ..utils.attributes import MOVE


class StopMove(RestrictionBase):
    title = "Randomly lock movement!"
    difficulty = 0
    hotkey_type = {"stop_position": [0]}
    attributes = [MOVE]

    interval = 50

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
                HotkeyManager().set_hotkeys("press_release", cls.hotkey_type)
            else:
                cls.lock_move = False
        elif randint(1, 400) == 1:
            cls.lock_end_time = time.time() + 3
            cls.lock_move = True
