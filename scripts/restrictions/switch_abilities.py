from random import choice, shuffle

from .restriction_hotkey_base import RestrictionHotkeyBase
from ..utils.attributes import ABILITY
from ..utils.constants import Constants


class SwitchAbilities(RestrictionHotkeyBase):
    title = "Switched ability hotkeys!"
    difficulty = 1
    attributes = [ABILITY]

    remap = {Constants.ABILITY: []}

    @classmethod
    def init(cls):
        hotkeys = [i for i in range(4)]
        switch_hotkeys = hotkeys.copy()
        cls.remap = {Constants.ABILITY: []}

        while [i for i in range(4) if hotkeys[i] == switch_hotkeys[i]]:
            shuffle(switch_hotkeys)

        for i in range(4):
            hotkey = hotkeys[i]
            switch_hotkey = switch_hotkeys[i]
            cls.remap[Constants.ABILITY].append((hotkey, switch_hotkey))

    @classmethod
    def restriction_content(cls):
        cls.hotkey_event(Constants.REMAP, cls.remap, True)

    @classmethod
    def on_end(cls):
        cls.hotkey_event(Constants.REMAP, cls.remap, False)
