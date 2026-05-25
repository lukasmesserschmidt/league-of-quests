from enum import Enum, auto


class QuestState(Enum):
    INACTIVE = auto()
    ACTIVE = auto()
    HOLDING = auto()
    COMPLETED = auto()
    FAILED = auto()
