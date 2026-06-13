from .quest import Quest
from ...restrictions import Restriction
from ....data import Config, QuestState
from ....game import GameContext


class HoldingQuest(Quest):
    holding_duration: float

    def __init__(self, config: Config, restriction: Restriction):
        super().__init__(config, restriction)
        self._holding_time_left = self.holding_duration

        self._condition_was_met = False

    def get_time_left(self):
        if self.get_state() == QuestState.CONDITION_MET:
            return self._holding_time_left
        return self._time_left

    def _update_time(self, dt: float):
        if self.get_state() != QuestState.CONDITION_MET:
            self._time_left -= dt
        else:
            self._holding_time_left -= dt

        if self._time_left <= 0:
            self.set_state(QuestState.FAILED)
        elif self._holding_time_left <= 0:
            self.set_state(QuestState.COMPLETED)

    def _update_condition(self, game_context: GameContext):
        condition_met = self._condition_met(game_context)
        if condition_met != self._condition_was_met:
            if condition_met:
                self.set_state(QuestState.CONDITION_MET)
                self._holding_time_left = (
                    self.holding_duration
                    if self._time_left > self.holding_duration
                    else self._time_left
                )
                self._restriction.deactivate()
                self._on_condition_met(game_context)
            else:
                self.set_state(QuestState.CONDITION_NOT_MET)
                self._restriction.activate()
                self._on_condition_not_met(game_context)
            self._condition_was_met = condition_met

    def _on_condition_met(self, game_context: GameContext):
        pass

    def _on_condition_not_met(self, game_context: GameContext):
        pass
