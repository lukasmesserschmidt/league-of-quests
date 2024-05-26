from random import randint

from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import ABILITY


class DisableUltimate(DisableHotkeyBase):
    title = "Ultimate is disabled!"
    difficulty = 1
    disable_hotkeys = {"ability": [3]}
    attributes = [ABILITY]
