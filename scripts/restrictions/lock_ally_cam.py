from random import randint

from .cycle_base import CycleBase
from .restriction_hotkey_base import RestrictionHotkeyBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.attributes import CAM
from ..utils.constants import Constants


class LockAllyCam(CycleBase, RestrictionHotkeyBase):
    title = "Randomly lock cam on teammate!"
    difficulty = 2
    attributes = [CAM]

    hotkey_types = {Constants.SELECT_ALLY: []}

    cycle_duration = 5

    @classmethod
    def check_dependencies(cls):
        return bool(ActivePlayerData.get_teammates())

    @classmethod
    def start_condition(cls):
        return randint(1, int(20000 / cls.interval)) == 1

    @classmethod
    def condition_met(cls):
        rand_ally = randint(0, len(ActivePlayerData.get_teammates()) - 1)
        cls.set_hotkey_types((Constants.SELECT_ALLY, [rand_ally]))

    @classmethod
    def cycle_content(cls):
        cls.hotkey_event(Constants.PRESS, cls.hotkey_types, True)

    @classmethod
    def cycle_end(cls):
        cls.hotkey_event(Constants.PRESS, cls.hotkey_types, False)
        cls.hotkey_event(Constants.PRESS_RELEASE, cls.hotkey_types)

    @classmethod
    def on_end(cls):
        cls.hotkey_event(Constants.PRESS, cls.hotkey_types, False)
        cls.hotkey_event(Constants.PRESS_RELEASE, cls.hotkey_types)
