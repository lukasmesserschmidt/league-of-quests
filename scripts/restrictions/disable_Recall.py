from .restriction_disable_hotkey_base import RestrictionDisableHotkeyBase
from ..utils.constants import Constants


class DisableRecall(RestrictionDisableHotkeyBase):
    title = "Recall is disabled!"
    difficulty = 1
    attributes = [Constants.RECALL]

    hotkey_types = {Constants.RECALL: [0]}
