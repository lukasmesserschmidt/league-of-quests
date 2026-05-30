from ...core import Quest
from ...core.states import Difficulty
from ...data import LiveClientData


class GetLevelQuest(Quest):
    description = "Get to level {target_level}."
    tags = ["level"]
    difficultys = Difficulty.MEDIUM
    duration = 300

    level_offset = 1

    @classmethod
    def requirements_met(cls, live_client_data: LiveClientData):
        return live_client_data.activePlayer.level <= 18 - cls.level_offset

    def _on_start(self, live_client_data: LiveClientData):
        self._current_level = live_client_data.activePlayer.level
        self._target_level = self._current_level + self.level_offset

        self.description = self.description.format(target_level=self._target_level)

    def _condition_met(self, live_client_data: LiveClientData) -> bool:
        self._current_level = live_client_data.activePlayer.level
        return self._current_level >= self._target_level

    def get_progress(self):
        return self._current_level

    def get_goal(self):
        return self._target_level


