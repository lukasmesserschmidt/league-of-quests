from .states import QuestState


class QuestClock:
    def __init__(self, max_duration: float, completion_time: float):
        self.time_left = max_duration
        self.completion_time_target = completion_time
        self.completion_time_left = completion_time

        self.state = QuestState.INACTIVE

    def update(self, dt: float, task_completed: bool):
        # reduce the remaining time
        if self.time_left > 0:
            self.time_left -= dt

        if self.state == QuestState.HOLDING:
            # currently in holding state, check if holding time has elapsed
            if self.completion_time_left > 0:
                self.completion_time_left -= dt
            else:
                # holding time completed, mark quest as completed
                self.state = QuestState.COMPLETED

    def activate_holding(self):
        self.state = QuestState.HOLDING
        self.completion_time_left = self.completion_time_target

    def deactivate_holding(self):
        self.state = QuestState.ACTIVE
        self.completion_time_left = self.completion_time_target
