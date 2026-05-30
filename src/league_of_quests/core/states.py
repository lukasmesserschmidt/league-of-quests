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
