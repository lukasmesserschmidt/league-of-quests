from ...core import Difficulty
from ...core import GameContext
from ...core.quests import Quest


class GetLevelQuest(Quest):
    description = "Get to level {target_level}."
    tags = ["level"]
    difficulty = Difficulty.MEDIUM
    duration = 300

    level_offset = 1

    @classmethod
    def requirements_met(cls, game_context: GameContext):
        return game_context.get_live_client_data().activePlayer.level <= 18 - cls.level_offset

    def _on_start(self, game_context: GameContext):
        self._current_level = game_context.get_live_client_data().activePlayer.level
        self._target_level = self._current_level + self.level_offset

        self.description = self.description.format(target_level=self._target_level)

    def _condition_met(self, game_context: GameContext) -> bool:
        self._current_level = game_context.get_live_client_data().activePlayer.level
        return self._current_level >= self._target_level

    def get_progress(self):
        return self._current_level

    def get_goal(self):
        return self._target_level
