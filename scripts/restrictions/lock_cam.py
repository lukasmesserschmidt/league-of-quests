from .restriction_thread_base import RestrictionThreadBase
from ..manager.hotkey_manager import HotkeyManager
from ..utils.attributes import CAM


class LockCam(RestrictionThreadBase):
    title = "Cam is locked!"
    difficulty = 0
    hotkey_type = {"snap_cam": [0]}
    attributes = [CAM]

    interval = 0.1

    @classmethod
    def init(cls):
        cls.hotkey_manager = HotkeyManager()

    @classmethod
    def restriction_content(cls):
        cls.hotkey_manager.hotkey_event("press", cls.hotkey_type, True)

    @classmethod
    def on_end(cls):
        cls.hotkey_manager.hotkey_event("press", cls.hotkey_type, False)
        del cls.hotkey_manager
