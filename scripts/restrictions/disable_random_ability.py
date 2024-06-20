from random import randint
import time

from .restriction_disable_hotkey_base import RestrictionDisableHotkeyBase
from ..utils.constants import Constants


# Idea from Daniel
class DisableRandomAbility(RestrictionDisableHotkeyBase):
    title = "Randomly change disabled ability!"
    difficulty = 2
    attributes = [Constants.ABILITY]

    hotkey_types = {Constants.ABILITY: []}

    change_time = 5

    @classmethod
    def init(cls):
        cls.change_time = time.time() + 5
        rand_ability = randint(0, 3)
        cls.set_hotkey_types((Constants.ABILITY, [rand_ability]))

    @classmethod
    def restriction_content(cls):
        cls.disable_hotkeys(True)

        if cls.change_time < time.time():
            cls.disable_hotkeys(False)
            cls.change_time = time.time() + 5
            rand_ability = randint(0, 3)
            cls.set_hotkey_types((Constants.ABILITY, [rand_ability]))
