from ...core import TaskEvaluator


class StatTaskEvaluator(TaskEvaluator):
    def _on_init(self, stat_type: str, target_value: float):
        self.stat_type = stat_type
        self.target_value = target_value

        self.start_value = None
        self.current_value = None

    def start(self, live_client_data):
        self.start_value = self._get_stat_value(live_client_data)

    def _evaluate_task(self, dt: float, live_client_data):
        self.current_value = self._get_stat_value(live_client_data)
        if self.start_value is None or self.current_value is None:
            return False
        return self.current_value - self.start_value >= self.target_value

    def _get_stat_value(self, live_client_data):
        return getattr(live_client_data, f"get_{self.stat_type}")()
