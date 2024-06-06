from .restriction_disable_hotkey_base import RestrictionDisableHotkeyBase
from ..utils.attributes import RECALL
from ..utils.constants import Constants


class DisableRecall(RestrictionDisableHotkeyBase):
    title = "Recall is disabled!"
    difficulty = 1
    attributes = [RECALL]

    hotkey_types = {Constants.RECALL: [0]}
