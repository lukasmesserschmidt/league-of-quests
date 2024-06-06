import time

from .cycle_base import CycleBase
from .disable_hotkey_base import DisableHotkeyBase
from ..common_classes.resource_base import ResouceBase
from ..utils.attributes import ABILITY, SUMMONER_SPELL
from ..utils.constants import Constants


class DisableOnDmgTaken(ResouceBase, CycleBase, DisableHotkeyBase):
    title = "Disable all on dmg taken!"
    difficulty = 2
    attributes = [ABILITY, SUMMONER_SPELL]

    resource_num = 0

    hotkey_types = {Constants.ABILITY: [0, 1, 2, 3], Constants.SUMMONER_SPELL: [0, 1]}

    cycle_duration = 1

    @classmethod
    def init(cls):
        cls.disable = False
        cls.disable_end_time = 0
        cls.last_health_diff = cls.get_resource_diff()

    @classmethod
    def restriction_content(cls):
        current_health_diff = cls.get_resource_diff()

        super().restriction_content(current_health_diff)

        cls.last_health_diff = current_health_diff

    @classmethod
    def start_condition(cls, *args):
        return cls.last_health_diff < args[0]

    @classmethod
    def cycle_content(cls):
        cls.disable_hotkey(True)

    @classmethod
    def cycle_end(cls):
        cls.disable_hotkey(False)
