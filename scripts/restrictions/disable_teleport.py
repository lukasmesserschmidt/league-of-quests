from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import TELEPORT


class DisableTeleport(DisableHotkeyBase):
    title = "Teleport is disabled!"
    difficulty = 0
    disable_hotkeys = {"teleport": [0]}
    attributes = [TELEPORT]
