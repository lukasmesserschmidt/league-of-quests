from abc import ABC, abstractmethod

from .. import Difficulty
from .. import GameDisruptor
from .. import GameContext


class Restriction(ABC):
    description: str
    difficulty: Difficulty
    tags: set[str]

    def __init__(self, game_disruptor: GameDisruptor):
        self._game_disruptor = game_disruptor

    @classmethod
    def requirements_met(cls, game_context: GameContext) -> bool:
        return True

    def start(self, game_context: GameContext):
        self._on_start(game_context)
        self.activate()

    def stop(self):
        self.deactivate()

    def update(self, dt: float, game_context: GameContext):
        self._on_update(dt, game_context)

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass

    def _on_start(self, game_context: GameContext):
        pass

    def _on_update(self, dt: float, game_context: GameContext):
        pass
