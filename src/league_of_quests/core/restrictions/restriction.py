from abc import ABC, abstractmethod

from .. import Difficulty
from .. import GameDisruptor
from ...data import LiveClientData
from ...data import LiveClientConfig


class Restriction(ABC):
    description: str
    difficulty: Difficulty
    tags: set[str]

    def __init__(self, game_disruptor: GameDisruptor):
        self._game_disruptor = game_disruptor

    @classmethod
    def requirements_met(
        cls, live_client_data: LiveClientData, live_client_config: LiveClientConfig
    ) -> bool:
        return True

    def start(self, live_client_data):
        self._on_start(live_client_data)
        self.activate()

    def stop(self):
        self.deactivate()

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass

    def _on_start(self, live_client_data):
        pass
