from random import randint
import time

from .restriction_thread_base import RestrictionThreadBase
from ..manager.hotkey_manager import HotkeyManager
from ..utils.attributes import CAM


class LockAllyCam(RestrictionThreadBase):
    title = "Randomly lock cam on ally!"
    difficulty = 2
    hotkey_type = {"select_ally": [0, 1, 2, 3]}
    attributes = [CAM]

    interval = 0.1

    lock_cam = False
    lock_end_time = 0

    @classmethod
    def init(cls):
        cls.lock_cam = False
        cls.lock_end_time = 0
        cls.hotkey_manager = HotkeyManager()

    @classmethod
    def restriction_content(cls):
        if cls.lock_cam:
            if time.time() < cls.lock_end_time:
                cls.hotkey_manager.set_hotkeys("press", cls.hotkey_type, True)
            else:
                cls.lock_cam = False
        elif randint(1, 200) == 1:
            cls.lock_end_time = time.time() + 5
            rand_ally = randint(0, 3)
            cls.hotkey_type = {"select_ally": [rand_ally]}
            cls.lock_cam = True
        else:
            cls.hotkey_manager.set_hotkeys("press", cls.hotkey_type, False)

    @classmethod
    def on_end(cls):
        cls.hotkey_manager.set_hotkeys("press", cls.hotkey_type, False)
        del cls.hotkey_manager
