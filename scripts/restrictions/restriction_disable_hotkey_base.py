from .restriction_hotkey_base import RestrictionHotkeyBase
from ..common_classes.enable_overlay_base import EnableOverlayBase
from ..gui.game_overlay.game_overlay_window import get_game_overlay
from ..utils.constants import Constants


class RestrictionDisableHotkeyBase(RestrictionHotkeyBase, EnableOverlayBase):

    @classmethod
    def restriction_content(cls):
        cls.disable_hotkeys(True)

    @classmethod
    def on_end(cls):
        cls.disable_hotkeys(False)

    @classmethod
    def disable_hotkeys(cls, enable: bool):
        cls.hotkey_event(Constants.DISABLE, cls.hotkey_types, enable)
        cls.enable_overlays(enable, cls.hotkey_types)
