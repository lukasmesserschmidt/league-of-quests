from abc import ABC

from ..core.enums import Difficulty
from ..core.game_context import GameContext


class GameEntity(ABC):
    description: str
    difficulty: Difficulty
    tags: list[str]

    def __init__(self):
        self._description = self.description

    def get_description(self):
        return self._description

    def _format_description(self, **kwargs):
        self._description = self.description.format(**kwargs)

    @classmethod
    def requirements_met(cls, game_context: GameContext) -> bool:
        return True
