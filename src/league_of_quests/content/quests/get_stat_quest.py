import random

from .base import HoldingQuest
from ...data import Difficulty
from ...game import GameContext


class GetStatQuest(HoldingQuest):
    description = "Get {value} {stat}."
    difficulty = Difficulty.EASY
    tags = ["stat"]
    duration = 360
    holding_duration = 20

    options = (
        {
            "key": "abilityPower",
            "value": 20,
            "display_name": "ability power",
        },
    )

    def _on_start(self, game_context: GameContext):
        option = random.choice(self.options)
        self._key = option["key"]
        self._target_value = option["value"]
        display_name = option["display_name"]

        self._format_description(value=self._target_value, stat=display_name)

        self._current_value = self._get_stat(game_context)
        self._start_value = self._current_value

    def _condition_met(self, game_context: GameContext) -> bool:
        self._current_value = self._get_stat(game_context)
        return (self._current_value - self._start_value) >= self._target_value

    def get_progress(self):
        return self._current_value - self._start_value

    def get_goal(self):
        return self._target_value

    def _get_stat(self, game_context: GameContext):
        return getattr(game_context.get_data().activePlayer.championStats, self._key, 0)
