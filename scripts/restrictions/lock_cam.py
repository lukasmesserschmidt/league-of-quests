from .restriction_hotkey_base import RestrictionHotkeyBase
from ..utils.attributes import CAM
from ..utils.constants import Constants


class LockCam(RestrictionHotkeyBase):
    title = "Cam is locked!"
    difficulty = 0
    hotkey_type = {Constants.SNAP_CAM: [0]}
    attributes = [CAM]

    @classmethod
    def restriction_content(cls):
        cls.hotkey_event(Constants.PRESS, cls.hotkey_type, True)

    @classmethod
    def on_end(cls):
        cls.hotkey_event(Constants.PRESS, cls.hotkey_type, False)
        cls.hotkey_event(Constants.PRESS_RELEASE, cls.hotkey_type)
