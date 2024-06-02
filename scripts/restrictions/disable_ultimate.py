from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import ABILITY
from ..utils.constants import Constants


class DisableUltimate(DisableHotkeyBase):
    title = "Ultimate is disabled!"
    difficulty = 1
    attributes = [ABILITY]

    hotkey_types = {Constants.ABILITY: [3]}
