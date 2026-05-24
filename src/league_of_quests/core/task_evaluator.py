from abc import ABC, abstractmethod

from ..data.live_client_data import LiveClientData


class TaskEvaluator(ABC):
    def __init__(self, max_duration: float, completion_time: float, **kwargs):
        self.time_left = max_duration  # Gesamte Lebenszeit der Quest
        self.completion_time_target = completion_time  # Wie lange muss gehalten werden?
        self.completion_timer = completion_time  # Der aktuelle Halte-Countdown

        self._is_holding = False
        self._is_completed = False
        self._is_failed = False

        self._on_init(**kwargs)

    def _on_init(self, **kwargs):
        """Called when the evaluator is initialized. Use this to set up any necessary state."""
        pass

    def is_completed(self):
        return self._is_completed

    def is_holding(self):
        return self._is_holding

    def is_failed(self):
        return self._is_failed

    def start(self, live_client_data: LiveClientData):
        """Called when the quest starts. Use this to initialize any necessary state."""
        pass

    def update(self, dt: float, live_client_data: LiveClientData):
        """Called repeatedly with the time delta and latest live client data."""
        if self._is_completed or self._is_failed:
            return

        # reduce the remaining time
        self.time_left -= dt
        if self.time_left <= 0:
            self._fail_task()
            return

        # compute if the task is currently completed
        task_completed = self._evaluate_task(dt, live_client_data)

        if not self._is_holding:
            # normal state: task is not currently held, check if it just got completed
            if task_completed:
                if self.completion_time_target > 0:
                    # task completed and switch to holding state, start completion timer
                    self._is_holding = True
                    self.completion_timer = self.completion_time_target
                else:
                    # task completed and no holding time defined, completed immediately
                    self._complete_task()
        else:
            # holding state: task was previously completed, check if it is still completed to continue the timer
            if task_completed:
                self.completion_timer -= dt
                if self.completion_timer <= 0:
                    # timer completed, quest is completed
                    self._complete_task()
            else:
                # task is no longer completed, exit holding state and reset timer
                self._is_holding = False
                self.completion_timer = self.completion_time_target

    @abstractmethod
    def _evaluate_task(self, dt: float, live_client_data: LiveClientData):
        """Evaluate the task's completion status."""

    def _complete_task(self):
        self._is_completed = True
        self._is_holding = False

    def _fail_task(self):
        self._is_failed = True
        self._is_holding = False
