from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import RECALL


class DisableRecall(DisableHotkeyBase):
    title = "Recall is disabled!"
    difficulty = 0
    disable_hotkeys = {"teleport": [0]}
    attributes = [RECALL]
