from .restriction_base import RestrictionBase
from ..manager.hotkey_manager import HotkeyManager
from ..utils.attributes import CAM


class LockCam(RestrictionBase):
    title = "Cam is locked!"
    difficulty = 1
    disable_hotkeys = {"snap_cam": [0]}
    attributes = [CAM]

    interval = 100

    @classmethod
    def init(cls):
        cls.hotkey_manager = HotkeyManager()

    @classmethod
    def restriction_content(cls):
        cls.hotkey_manager.set_hotkeys("press", cls.disable_hotkeys, True)

    @classmethod
    def on_end(cls):
        cls.hotkey_manager.set_hotkeys("press", cls.disable_hotkeys, False)
        del cls.hotkey_manager
