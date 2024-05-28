from random import choice, shuffle

from .restriction_base import RestrictionBase
from ..manager.hotkey_manager import HotkeyManager, EventType
from ..utils.attributes import ABILITY


class SwitchAbilities(RestrictionBase):
    title = "Switched ability hotkeys!"
    difficulty = 1
    remap = {"ability": []}
    attributes = [ABILITY]

    @classmethod
    def init(cls):
        cls.hotkey_manager = HotkeyManager()

        hotkeys = [i for i in range(4)]
        switch_hotkeys = hotkeys.copy()
        cls.remap = {"ability": []}

        while [i for i in range(4) if hotkeys[i] == switch_hotkeys[i]]:
            shuffle(switch_hotkeys)

        for i in range(4):
            hotkey = hotkeys[i]
            switch_hotkey = switch_hotkeys[i]
            cls.remap["ability"].append((hotkey, switch_hotkey))

    @classmethod
    def restriction_content(cls):
        cls.hotkey_manager.hotkey_event(EventType.REMAP, cls.remap, True)

    @classmethod
    def on_end(cls):
        cls.hotkey_manager.hotkey_event(EventType.REMAP, cls.remap, False)
        del cls.hotkey_manager
