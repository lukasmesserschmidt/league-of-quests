from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import TRINKET
from ..utils.constants import Constants


class DisableTrinket(DisableHotkeyBase):
    title = "Trinket is disabled!"
    difficulty = 0
    attributes = [TRINKET]

    disable_hotkeys = {Constants.TRINKET: [0]}
