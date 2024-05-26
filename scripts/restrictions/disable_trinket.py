from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import TRINKET


class DisableTrinket(DisableHotkeyBase):
    title = "Trinket is disabled!"
    difficulty = 0
    disable_hotkeys = {"trinket": [0]}
    attributes = [TRINKET]
