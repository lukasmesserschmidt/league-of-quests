from .restriction_disable_hotkey_base import RestrictionDisableHotkeyBase
from ..utils.constants import Constants


class DisableTrinket(RestrictionDisableHotkeyBase):
    title = "Trinket is disabled!"
    difficulty = 0
    attributes = [Constants.TRINKET]

    hotkey_types = {Constants.TRINKET: [0]}
