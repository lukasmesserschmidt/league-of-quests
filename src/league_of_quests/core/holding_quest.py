from .quest import Quest
from .states import QuestState
from ..data import LiveClientData
from ..core.restriction import Restriction


class HoldingQuest(Quest):
    holding_duration: float

    def __init__(self, restriction: Restriction):
        super().__init__(restriction)
        self._holding_time_left = self.holding_duration

        self._condition_was_met = False

    def get_time_left(self):
        if self.get_state() == QuestState.CONDITION_MET:
            return self._holding_time_left
        return self._time_left

    def _update_time(self, dt: float):
        if self.get_state() == QuestState.CONDITION_NOT_MET:
            self._time_left -= dt
        elif self.get_state() == QuestState.CONDITION_MET:
            self._holding_time_left -= dt

        if self._time_left <= 0:
            self.set_state(QuestState.FAILED)
        elif self._holding_time_left <= 0:
            self.set_state(QuestState.COMPLETED)

    def _update_condition(self, live_client_data: LiveClientData):
        condition_met = self._condition_met(live_client_data)
        if condition_met != self._condition_was_met:
            if condition_met:
                self.set_state(QuestState.CONDITION_MET)
                self._holding_time_left = self.holding_duration
                self._on_condition_met(live_client_data)
            else:
                self.set_state(QuestState.CONDITION_NOT_MET)
                self._on_condition_not_met(live_client_data)
            self._condition_was_met = condition_met

    def _on_condition_met(self, live_client_data: LiveClientData):
        pass

    def _on_condition_not_met(self, live_client_data: LiveClientData):
        pass

