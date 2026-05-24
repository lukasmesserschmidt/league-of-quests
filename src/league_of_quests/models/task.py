from ..core import TaskEvaluator


class Task:
    def __init__(
        self, id: str, description: str, tags: list[str], evaluator: TaskEvaluator
    ):
        self.id = id
        self.description = description
        self.tags = tags
        self._evaluator = evaluator

    def start(self, live_client_data):
        self._evaluator.start(live_client_data)

    def update(self, dt: float, live_client_data):
        self._evaluator.update(dt, live_client_data)
