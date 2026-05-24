from .task import Task
from .restriction import Restriction
from ..data import LiveClientData


class Quest:
    def __init__(self, task: Task, restriction: Restriction):
        self._task = task
        self._restriction = restriction

        self._is_completed = False
        self._is_failed = False

        self._restriction_paused = False

    def is_completed(self):
        return self._is_completed

    def is_failed(self):
        return self._is_failed

    def start(self, live_client_data: LiveClientData):
        self._task._evaluator.start(live_client_data)
        # Restriction initialization can be added here

    def update(self, dt: float, live_client_data: LiveClientData):
        if self._is_completed or self._is_failed:
            return

        self._task.update(dt, live_client_data)

        evaluator = self._task._evaluator
        if evaluator.is_holding():
            # deactivate restriction if holding state and not already paused
            if not self._restriction_paused:
                self._restriction.deactivate()
                self._restriction_paused = True
        else:
            # reactivate restriction if not in holding state but is currently paused
            if self._restriction_paused:
                self._restriction.activate()
                self._restriction_paused = False

        # update restriction if not paused
        if not self._restriction_paused:
            self._restriction.update(dt)

        # check for quest completion or failure
        if evaluator.is_failed():
            self._fail_quest()
        elif evaluator.is_completed():
            self._complete_quest()

    def _complete_quest(self):
        self._is_completed = True
        self._restriction.deactivate()

    def _fail_quest(self):
        self._is_failed = True
        self._restriction.deactivate()
