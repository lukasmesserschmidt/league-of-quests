from abc import abstractmethod

from .. import QuestState
from .. import GameContext
from ..restrictions import Restriction
from ...data import Config
from .. import GameEntity


class Quest(GameEntity):
    duration: float

    def __init__(self, config: Config, restriction: Restriction):
        self._description = self.description
        self._duration = self.duration * config.quests.duration_factor
        self._time_left = self._duration
        self._state = QuestState.INACTIVE

        self._restriction = restriction

    def get_restriction(self):
        return self._restriction

    def get_time_left(self):
        return self._time_left

    def get_state(self):
        return self._state

    def set_state(self, state: QuestState):
        self._state = state

    def start(self, game_context: GameContext):
        self.set_state(QuestState.ACTIVE)
        self._on_start(game_context)
        self._restriction.start(game_context)

    def stop(self):
        self._restriction.stop()

    def update(self, dt: float, game_context: GameContext):
        if self.get_state() not in (
            QuestState.INACTIVE,
            QuestState.COMPLETED,
            QuestState.FAILED,
        ):
            self._update_time(dt)
            self._update_condition(game_context)
            self._restriction.update(dt, game_context)

    def _update_time(self, dt: float):
        self._time_left -= dt
        if self._time_left <= 0:
            self.set_state(QuestState.FAILED)

    def _update_condition(self, game_context: GameContext):
        condition_met = self._condition_met(game_context)
        if condition_met:
            self.set_state(QuestState.COMPLETED)

    @abstractmethod
    def get_progress(self):
        pass

    @abstractmethod
    def get_goal(self):
        pass

    @abstractmethod
    def _condition_met(self, game_context: GameContext) -> bool:
        pass
