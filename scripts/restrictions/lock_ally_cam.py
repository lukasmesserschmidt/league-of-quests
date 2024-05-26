from random import randint
import time

from .restriction_thread_base import RestrictionThreadBase
from ..manager.hotkey_manager import HotkeyManager
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.attributes import CAM


class LockAllyCam(RestrictionThreadBase):
    title = "Randomly lock cam on teammate!"
    difficulty = 2
    hotkey_type = {"select_ally": []}
    attributes = [CAM]

    interval = 0.2

    lock_cam = False
    lock_end_time = 0

    @classmethod
    def check_dependencies(cls):
        return bool(ActivePlayerData.get_teammates())

    @classmethod
    def init(cls):
        cls.lock_cam = False
        cls.lock_end_time = 0
        cls.hotkey_manager = HotkeyManager()

    @classmethod
    def restriction_content(cls):
        if cls.lock_cam:
            if time.time() < cls.lock_end_time:
                cls.hotkey_manager.hotkey_event("press", cls.hotkey_type, True)
            else:
                cls.hotkey_manager.hotkey_event("press", cls.hotkey_type, False)
                cls.lock_cam = False
        elif randint(1, 100) == 1:
            cls.lock_end_time = time.time() + 5
            rand_ally = randint(0, len(ActivePlayerData.get_teammates()) - 1)
            cls.hotkey_type = {"select_ally": [rand_ally]}
            cls.lock_cam = True

    @classmethod
    def on_end(cls):
        cls.hotkey_manager.hotkey_event("press", cls.hotkey_type, False)
        del cls.hotkey_manager
