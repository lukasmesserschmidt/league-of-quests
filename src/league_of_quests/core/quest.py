from abc import ABC, abstractmethod

from .restriction import Restriction
from .states import Difficulty, QuestState
from ..data import LiveClientData


class Quest(ABC):
    describtion: str
    difficultys: Difficulty
    tags: list[str]

    duration: float

    def __init__(self, restriction: Restriction):
        self._duration = self.duration
        self._time_left = self._duration
        self._state = QuestState.INACTIVE

        self._restriction = restriction

    def get_time_left(self):
        return self._time_left

    def get_state(self):
        return self._state

    def set_state(self, state: QuestState):
        self._state = state

    def start(self, live_client_data: LiveClientData):
        self.set_state(QuestState.ACTIVE)
        self._on_start(live_client_data)

    def update(self, dt: float, live_client_data: LiveClientData):
        if self.get_state() not in (QuestState.INACTIVE, QuestState.COMPLETED, QuestState.FAILED):
            self._update_time(dt)
            self._update_condition(live_client_data)

    def _update_time(self, dt: float):
        self._time_left -= dt
        if self._time_left <= 0:
            self.set_state(QuestState.FAILED)

    def _update_condition(self, live_client_data: LiveClientData):
        condition_met = self._condition_met(live_client_data)
        if condition_met:
            self.set_state(QuestState.COMPLETED)

    @abstractmethod
    def get_progress(self):
        pass

    @abstractmethod
    def get_goal(self):
        pass

    @classmethod
    def requirements_met(cls, live_client_data: LiveClientData):
        return True

    def _on_start(self, live_client_data: LiveClientData):
        pass

    @abstractmethod
    def _condition_met(self, live_client_data: LiveClientData) -> bool:
        pass
