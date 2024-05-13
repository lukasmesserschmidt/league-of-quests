from random import choice

from .restriction_base import RestrictionBase
from ..manager.hotkey_manager import HotkeyManager
from ..utils.attributes import ABILITY


class SwitchAbilities(RestrictionBase):
    title = "Switched ability hotkeys!"
    difficulty = 1
    attributes = [ABILITY]

    @classmethod
    def init(cls):
        cls.hotkey_manager = HotkeyManager()

        hotkeys = [i for i in range(4)]
        switch_hotkeys = hotkeys.copy()
        cls.remap = {"ability": []}

        for hotkey in hotkeys:
            switch_hotkey = choice(switch_hotkeys)
            while switch_hotkey == hotkey:
                switch_hotkey = choice(switch_hotkeys)
            switch_hotkeys.remove(switch_hotkey)

            cls.remap["ability"].append((hotkey, switch_hotkey))

    @classmethod
    def restriction_content(cls):
        cls.hotkey_manager.set_hotkeys("remap", cls.remap, True)

    @classmethod
    def on_end(cls):
        cls.hotkey_manager.set_hotkeys("remap", cls.remap, False)
        del cls.hotkey_manager
