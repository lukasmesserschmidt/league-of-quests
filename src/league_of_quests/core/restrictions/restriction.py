from abc import ABC, abstractmethod

from .. import Difficulty


class Restriction(ABC):
    description: str
    difficulty: Difficulty
    tags: set[str]

    def requirements_met(self, live_client_data) -> bool:
        return True

    def start(self, live_client_data):
        pass

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass

    def update(self, live_client_data):
        pass
