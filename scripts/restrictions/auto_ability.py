from random import randint

from .restriction_hotkey_base import RestrictionHotkeyBase
from ..utils.constants import Constants
from ..utils.attributes import ABILITY, AUTO
from ..utils.constants import Constants


class AutoAbility(RestrictionHotkeyBase):
    title = "Auto cast random abilities!"
    difficulty = 2
    attributes = [ABILITY, AUTO]

    hotkey_types = {Constants.ABILITY: [], Constants.QUICK_ABILITY: []}

    @classmethod
    def restriction_content(cls):
        if randint(1, int(5000 / cls.interval)) == 1:
            rand_ability = randint(0, 3)
            cls.set_hotkey_types(
                (Constants.ABILITY, [rand_ability]),
                (Constants.QUICK_ABILITY, [rand_ability]),
            )

            cls.hotkey_event(Constants.PRESS_RELEASE, cls.hotkey_types)
