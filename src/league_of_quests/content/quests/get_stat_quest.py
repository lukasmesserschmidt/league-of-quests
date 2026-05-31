import random

from ...data import LiveClientData
from ...core import Difficulty
from ...core.quests import HoldingQuest


class GetStatQuest(HoldingQuest):
    description = "Get {value} {stat}."
    difficulty = Difficulty.EASY
    tags = ["stat"]
    duration = 300
    holding_duration = 20

    options = (
        {
            "key": "abilityPower",
            "value": 20,
            "display_name": "ability power",
        },
    )

    def _on_start(self, live_client_data: LiveClientData):
        option = random.choice(self.options)
        self._key = option["key"]
        self._target_value = option["value"]
        self._display_name = option["display_name"]

        self.description = self.description.format(
            value=self._target_value, stat=self._display_name
        )

        value = self._get_stat(live_client_data)
        self._start_value = value
        self._current_value = value

    def _condition_met(self, live_client_data: LiveClientData) -> bool:
        self._current_value = self._get_stat(live_client_data)
        return self._current_value >= self._target_value

    def get_progress(self):
        return self._current_value

    def get_goal(self):
        return self._target_value

    def _get_stat(self, live_client_data: LiveClientData):
        return getattr(live_client_data.activePlayer.championStats, self._key, 0)
