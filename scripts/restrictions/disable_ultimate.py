from .restriction_disable_hotkey_base import RestrictionDisableHotkeyBase
from ..utils.constants import Constants


class DisableUltimate(RestrictionDisableHotkeyBase):
    title = "Ultimate is disabled!"
    difficulty = 1
    attributes = [Constants.ABILITY]

    hotkey_types = {Constants.ABILITY: [3]}
