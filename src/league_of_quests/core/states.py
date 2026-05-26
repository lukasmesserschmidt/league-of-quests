from enum import Enum, auto


class QuestState(Enum):
    INACTIVE = auto()
    ACTIVE = auto()
    HOLDING = auto()
    CONDITION_MET = auto()
    COMPLETED = auto()
    FAILED = auto()

class ClockState(Enum):
    INACTIVE = auto()
    ACTIVE = auto()
    HOLDING = auto()
    TIMER_EXPIRED = auto()

class Difficulty(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()
