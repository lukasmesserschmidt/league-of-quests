import time

from .cycle_base import CycleBase
from .restriction_disable_hotkey_base import RestrictionDisableHotkeyBase
from ..common_classes.resource_base import ResouceBase
from ..utils.constants import Constants


class DisableOnDmgTaken(ResouceBase, CycleBase, RestrictionDisableHotkeyBase):
    title = "Disable all on dmg taken!"
    difficulty = 2
    attributes = [Constants.ABILITY, Constants.SUMMONER_SPELL]

    resource_num = 0

    hotkey_types = {Constants.ABILITY: [0, 1, 2, 3], Constants.SUMMONER_SPELL: [0, 1]}

    cycle_duration = 2

    @classmethod
    def init(cls):
        cls.last_health_diff = cls.get_resource_diff()

    @classmethod
    def restriction_content(cls):
        cls.current_health_diff = cls.get_resource_diff()

        super().restriction_content()

        cls.last_health_diff = cls.current_health_diff

    @classmethod
    def start_condition(cls):
        return cls.last_health_diff < cls.current_health_diff

    @classmethod
    def cycle_content(cls):
        cls.disable_hotkeys(True)

    @classmethod
    def cycle_end(cls):
        cls.disable_hotkeys(False)
