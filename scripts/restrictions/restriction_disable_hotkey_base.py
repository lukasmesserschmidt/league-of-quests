from .restriction_hotkey_base import RestrictionHotkeyBase
from ..gui.game_overlay.game_overlay_window import get_game_overlay
from ..utils.constants import Constants


class RestrictionDisableHotkeyBase(RestrictionHotkeyBase):

    @classmethod
    def restriction_content(cls):
        cls.disable_hotkeys(True)

    @classmethod
    def on_end(cls):
        cls.disable_hotkeys(False)

    @classmethod
    def disable_hotkeys(cls, enable: bool):
        cls.hotkey_event(Constants.DISABLE, cls.hotkey_types, enable)
        get_game_overlay().enable_cover(enable, cls.hotkey_types)
