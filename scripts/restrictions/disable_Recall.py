from .disable_hotkey_base import DisableHotkeyBase
from ..utils.attributes import RECALL
from ..utils.constants import Constants


class DisableRecall(DisableHotkeyBase):
    title = "Recall is disabled!"
    difficulty = 0
    attributes = [RECALL]

    hotkey_types = {Constants.TELEPORT: [0]}
