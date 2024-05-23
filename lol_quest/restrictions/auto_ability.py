from random import randint

from .restriction_base import RestrictionBase
from ..manager.hotkey_manager import HotkeyManager

from ..utils.attributes import ABILITY, AUTO


class AutoAbility(RestrictionBase):
    title = "Auto cast random abilities!"
    difficulty = 2
    attributes = [ABILITY, AUTO]

    @classmethod
    def restriction_content(cls):
        if randint(1, 60) == 1:
            rand_ability = randint(0, 3)
            hotkey_type = {"quick_ability": [rand_ability]}
            HotkeyManager().set_hotkeys("press_release", hotkey_type)
            hotkey_type = {"ability": [rand_ability]}
            HotkeyManager().set_hotkeys("press_release", hotkey_type)
