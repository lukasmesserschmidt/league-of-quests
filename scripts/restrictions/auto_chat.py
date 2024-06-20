from random import randint, choice
import time

from .restriction_base import RestrictionBase
from ..manager.hotkey_manager import HotkeyManager
from ..utils.constants import Constants


class AutoChat(RestrictionBase):
    title = "Auto chat!"
    difficulty = 2
    attributes = [Constants.CHAT, Constants.AUTO]

    delay = 0

    messages = tilt_messages = [
        "Feeding hard, top? Nice job.",
        "Blind jungle, ever heard of ganking?",
        "Feeding more than a bot, bot lane.",
        "Top lane is a joke.",
        "Mid, did you forget how to CS?",
        "Jungle, do you even know what Smite is?",
        "Bot, nice inting spree.",
        "Top, you’re a walking feeder.",
        "Mid, you’re the reason we lose.",
        "Jungle, your map awareness is a joke.",
        "Bot lane, ever heard of vision?",
        "Mid, you play like a potato.",
        "Jungle, thanks for the free loss.",
        "Bot, are you playing with a blindfold?",
        "Top, congrats on being useless.",
        "Mid, did your brain DC?",
        "Bot, you make feeding an art form.",
        "Mid, your CS is laughable.",
        "Bot, your ADC skills are tragic.",
        "Top, do you even know how to lane?",
        "Mid, ever heard of roaming?",
        "Bot, your support is a liability.",
        "Top, stop feeding and start playing.",
        "Mid, do you know what map awareness is?",
        "Jungle, you’ve been AFK all game.",
        "Top, your gameplay is a meme.",
        "Mid, you’re just a free kill.",
        "Jungle, where’s the Smite when you need it?",
        "Top, your TP plays are trash.",
        "Mid, nice int, keep it up.",
        "Jungle, you missed another dragon.",
        "Bot, you’re just a gold bag for the enemy.",
        "Top, why even bother showing up?",
        "Mid, you’re the definition of useless.",
        "Jungle, stop farming and start ganking.",
        "Bot, is this your first game?",
        "Top, more deaths than cs.",
        "Jungle, another failed gank, surprise.",
        "Bot, you belong in Bronze.",
        "Top, your feeding skills are unmatched.",
    ]

    @classmethod
    def init(cls):
        cls.remaining_messages = cls.messages.copy()

    @classmethod
    def restriction_content(cls):
        if time.time() < cls.delay:
            pass
        elif randint(1, int(25000 / cls.interval)) == 1:
            if len(cls.remaining_messages) <= 0:
                cls.remaining_messages = cls.messages.copy()

            rand_message = randint(0, len(cls.remaining_messages) - 1)
            message = cls.remaining_messages.pop(rand_message)
            HotkeyManager.write_chat(message)
            cls.delay = time.time() + 15
