from random import randint

from .restriction_disable_hotkey_base import RestrictionDisableHotkeyBase
from ..common_classes.resource_base import ResouceBase
from ..utils.constants import Constants


class DisableBelowResourceValue(ResouceBase, RestrictionDisableHotkeyBase):
    title = "Disable all if below 40% ?!"
    difficulty = None
    attributes = [Constants.RESOURCE, Constants.ABILITY, Constants.SUMMONER_SPELL]

    alternating_difficulties = (0, 1, 2)

    resource_num = 1

    overlay_types = {Constants.RESOURCE: []}

    hotkey_types = {Constants.ABILITY: [0, 1, 2, 3], Constants.SUMMONER_SPELL: [0, 1]}

    disable = False

    @classmethod
    def init(cls):
        cls.percent_threshold = 0.2 * (cls.difficulty + 1)
        cls.set_overlay_type(
            (Constants.RESOURCE, [(cls.resource_num, cls.percent_threshold)])
        )

        percent_text = 20 * (cls.difficulty + 1)
        resource_type = cls.get_resource_data()["type"]
        cls.title = f"Disable all if below {percent_text}% {resource_type.upper()}!"

    @classmethod
    def restriction_content(cls):
        resource_data = cls.get_resource_data()
        cls.enable_overlays(True)

        if cls.get_percent(resource_data) < cls.percent_threshold:
            cls.disable_hotkeys(True)
            cls.disable = True
        elif cls.disable:
            cls.disable_hotkeys(False)
            cls.disable = False

    @classmethod
    def on_end(cls):
        super().on_end()
        cls.enable_overlays(False)
