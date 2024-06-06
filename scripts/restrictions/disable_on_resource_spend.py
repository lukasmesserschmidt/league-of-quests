import time

from .cycle_base import CycleBase
from .restriction_disable_hotkey_base import RestrictionDisableHotkeyBase
from ..common_classes.resource_base import ResouceBase
from ..utils.attributes import ABILITY, SUMMONER_SPELL
from ..utils.constants import Constants


class DisableOnResourceSpend(ResouceBase, CycleBase, RestrictionDisableHotkeyBase):
    title = "Disable all on ? spend!"
    difficulty = 2
    attributes = [ABILITY, SUMMONER_SPELL]

    resource_num = 1

    cycle_duration = 2

    hotkey_types = {Constants.ABILITY: [0, 1, 2, 3], Constants.SUMMONER_SPELL: [0, 1]}

    @classmethod
    def init(cls):
        super().init()
        cls.last_resource_diff = cls.get_resource_diff()
        resource_type = cls.get_resource_data()["type"]
        cls.title = f"Disable all on {resource_type.upper()} spend!"

    @classmethod
    def restriction_content(cls):
        cls.current_resource_diff = cls.get_resource_diff()

        super().restriction_content()

        cls.last_resource_diff = cls.current_resource_diff

    @classmethod
    def start_condition(cls):
        return cls.last_resource_diff < cls.current_resource_diff

    @classmethod
    def cycle_content(cls):
        cls.disable_hotkeys(True)

    @classmethod
    def cycle_end(cls):
        cls.disable_hotkeys(False)
