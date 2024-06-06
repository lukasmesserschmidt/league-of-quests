from random import choice, shuffle

from .restriction_hotkey_base import RestrictionHotkeyBase
from ..utils.attributes import ABILITY
from ..utils.constants import Constants


class SwitchAbilities(RestrictionHotkeyBase):
    title = "Switched ability hotkeys!"
    difficulty = 1
    attributes = [ABILITY]

    hotkey_types = {Constants.ABILITY: []}

    @classmethod
    def init(cls):
        hotkeys = [i for i in range(4)]
        switch_hotkeys = hotkeys.copy()
        hotkey_nums = []

        while [i for i in range(4) if hotkeys[i] == switch_hotkeys[i]]:
            shuffle(switch_hotkeys)

        for hotkey, switch_hotkey in zip(hotkeys, switch_hotkeys):
            hotkey_nums.append((hotkey, switch_hotkey))

        cls.set_hotkey_types((Constants.ABILITY, hotkey_nums))

    @classmethod
    def restriction_content(cls):
        cls.hotkey_event(Constants.REMAP, cls.hotkey_types, True)

    @classmethod
    def on_end(cls):
        cls.hotkey_event(Constants.REMAP, cls.hotkey_types, False)
