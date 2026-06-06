from pydantic import BaseModel


DEFAULT_CONFIG = {
    "quests": {
        "limit": 2,
        "duration_scale": 1.0,
        "new_quest_on_death": True,
        "new_quest_on_fail": False,
        "new_quest_after_time": False,
        "new_quest_after_time_interval": 240,
        "allow_similar": False,
        "difficulties": {"easy": 0.6, "medium": 0.3, "hard": 0.1},
    },
    "restrictions": {
        "allow_similar": False,
        "difficulties": {"easy": 0.6, "medium": 0.3, "hard": 0.1},
    },
}


class Difficulties(BaseModel):
    easy: float
    medium: float
    hard: float


class Quests(BaseModel):
    limit: int
    duration_factor: float
    new_quest_on_death: bool
    new_quest_on_fail: bool
    new_quest_after_time: bool
    new_quest_after_time_interval: int
    allow_similar: bool
    difficulties: Difficulties


class Restrictions(BaseModel):
    allow_similar: bool
    difficulties: Difficulties


class Config(BaseModel):
    quests: Quests
    restrictions: Restrictions
