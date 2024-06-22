"""
This module contains the RestrictionDisableHotkeyBase class.
"""

from .restriction_hotkey_base import RestrictionHotkeyBase
from ..common_classes.enable_overlay_base import EnableOverlayBase
from ..utils.constants import Constants


class RestrictionDisableHotkeyBase(RestrictionHotkeyBase, EnableOverlayBase):
    """
    This class is a base class for all restrictions that disable hotkeys.
    """

    @classmethod
    def restriction_content(cls):
        cls.disable_hotkeys(True)

    @classmethod
    def on_end(cls):
        cls.disable_hotkeys(False)

    @classmethod
    def disable_hotkeys(cls, enable: bool):
        """
        Disables or enables the hotkeys deffined in the hotkey_types.
        """
        cls.hotkey_event(Constants.DISABLE, cls.hotkey_types, enable)
        cls.enable_overlays(enable, cls.hotkey_types)
