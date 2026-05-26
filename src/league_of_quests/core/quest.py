from abc import ABC, abstractmethod

from .clock import Clock
from .restriction import Restriction
from .states import Difficulty, QuestState
from ..data import LiveClientData


class Quest(ABC):
    describtion: str
    difficultys: list[Difficulty]
    tags: list[str]
    
    def __init__(self, duration: float, difficulty: Difficulty, restriction: Restriction):
        self._clock = Clock(duration)
        self._state = QuestState.INACTIVE

        self._difficulty = difficulty

        self._restriction = restriction
        self._restriction_paused = False

        self._on_init()

    def _on_init(self):
        pass

    def is_completed(self):
        return self._state == QuestState.COMPLETED

    def is_failed(self):
        return self._state == QuestState.FAILED

    def is_holding(self):
        return self._clock.is_holding()

    def get_state(self):
        return self._state

    def set_state(self, state: QuestState):
        self._state = state

    def get_time_left(self):
        return self._clock.get_time_left()

    def get_completion_time_left(self):
        return self._clock.get_holding_time_left()

    @staticmethod
    def conditions_met(live_client_data: LiveClientData):
        return True

    def start(self, live_client_data: LiveClientData):
        pass

    def update(self, dt: float, live_client_data: LiveClientData):
        if self.is_completed() or self.is_failed():
            return

        self._clock.update(dt)
        self._on_update(dt, live_client_data)
        
    @abstractmethod
    def _on_update(self, dt: float, live_client_data: LiveClientData):
        pass
        
    @abstractmethod
    def get_progress(self):
        pass

    @abstractmethod
    def get_goal(self):
        pass


