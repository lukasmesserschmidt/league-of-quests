from ...quest_clock import QuestClock
from .task_evaluator import TaskEvaluator
from .restriction_effect import RestrictionEffect
from ....data import LiveClientData


class Quest:
    def __init__(
        self,
        quest_clock: QuestClock,
        task_evaluator: TaskEvaluator,
        restriction_effect: RestrictionEffect,
    ):
        self._quest_clock = quest_clock
        self._task_evaluator = task_evaluator
        self._restriction_effect = restriction_effect

        self._is_completed = False
        self._is_failed = False

        self._restriction_paused = False

    def is_completed(self):
        return self._is_completed

    def is_failed(self):
        return self._is_failed

    def is_holding(self):
        return self._task_evaluator.is_holding()

    def get_time_left(self):
        return self._task_evaluator.get_time_left()

    def get_completion_time_left(self):
        return self._task_evaluator.get_completion_time_left()

    def get_progress(self):
        return self._task_evaluator.get_progress()

    def get_goal(self):
        return self._task_evaluator.get_goal()

    def start(self, live_client_data: LiveClientData):
        self._task_evaluator.start(live_client_data)
        # Restriction initialization can be added here

    def update(self, dt: float, live_client_data: LiveClientData):
        if self._is_completed or self._is_failed:
            return

        self._quest_clock.update(dt)

        self._task_evaluator.update(dt, live_client_data)

        if self._task_evaluator.is_holding():
            # deactivate restriction if holding state and not already paused
            if not self._restriction_paused:
                self._restriction_effect.deactivate()
                self._restriction_paused = True
        else:
            # reactivate restriction if not in holding state but is currently paused
            if self._restriction_paused:
                self._restriction_effect.activate()
                self._restriction_paused = False

        # update restriction if not paused
        if not self._restriction_paused:
            self._restriction_effect.update(dt)

        # check for quest completion or failure
        if self._task_evaluator.is_failed():
            self._fail_quest()
        elif self._task_evaluator.is_completed():
            self._complete_quest()

    def _complete_quest(self):
        self._is_completed = True
        self._restriction_effect.deactivate()

    def _fail_quest(self):
        self._is_failed = True
        self._restriction_effect.deactivate()
