from enum import Enum, auto


class QuestState(Enum):
    INACTIVE = auto()
    ACTIVE = auto()
    CONDITION_MET = auto()
    CONDITION_NOT_MET = auto()
    COMPLETED = auto()
    FAILED = auto()


class Difficulty(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()


class HotkeyType(Enum):
    ABILITY_1 = "evtCastSpell1"
    ABILITY_2 = "evtCastSpell2"
    ABILITY_3 = "evtCastSpell3"
    ULT = "evtCastSpell4"
    SUMMONER_SPELL_1 = "evtCastAvatarSpell1"
    SUMMONER_SPELL_2 = "evtCastAvatarSpell2"
    WARD = "evtUseVisionItem"
