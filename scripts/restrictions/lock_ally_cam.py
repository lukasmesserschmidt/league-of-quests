from random import randint
import time

from .restriction_hotkey_base import RestrictionHotkeyBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.attributes import CAM
from ..utils.constants import Constants


class LockAllyCam(RestrictionHotkeyBase):
    title = "Randomly lock cam on teammate!"
    difficulty = 2
    attributes = [CAM]

    hotkey_types = {Constants.SELECT_ALLY: []}

    lock_cam = False
    lock_end_time = 0

    @classmethod
    def check_dependencies(cls):
        return bool(ActivePlayerData.get_teammates())

    @classmethod
    def init(cls):
        cls.lock_cam = False
        cls.lock_end_time = 0

    @classmethod
    def restriction_content(cls):
        if cls.lock_cam:
            if time.time() < cls.lock_end_time:
                cls.hotkey_event(Constants.PRESS, cls.hotkey_types, True)
            else:
                cls.hotkey_event(Constants.PRESS, cls.hotkey_types, False)
                cls.lock_cam = False
        elif randint(1, int(20000 / cls.interval)) == 1:
            cls.lock_end_time = time.time() + 5
            rand_ally = randint(0, len(ActivePlayerData.get_teammates()) - 1)
            cls.hotkey_types = {Constants.SELECT_ALLY: [rand_ally]}
            cls.lock_cam = True

    @classmethod
    def on_end(cls):
        cls.hotkey_event(Constants.PRESS, cls.hotkey_types, False)
