from abc import abstractmethod

from ... import GameEntity
from ....game import GameDisruptor, GameContext


class Restriction(GameEntity):
    def __init__(self, game_disruptor: GameDisruptor):
        self._game_disruptor = game_disruptor

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

    def _on_update(self, dt: float, game_context: GameContext):
        pass
