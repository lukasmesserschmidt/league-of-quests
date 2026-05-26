from ...data import LiveClientData
from ...core import Quest
from ...core.states import Difficulty
import random


class GetStatQuest(Quest):
    description = "Get {value} {stat}."
    difficultys = [Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD]
    tags = ["stat"]

    options = (
        {"key": "abilityPower", "values": {Difficulty.EASY: 20, Difficulty.MEDIUM: 40, Difficulty.HARD: 60}},
    )
    
    def _on_init(self):
        option = random.choice(self.options)
        self._key = option["key"]
        self._target_value = option["values"][self._difficulty]

        self.description = self.description.format(value=self._target_value, stat=self._key)

        self._start_value = 0
        self._current_value = 0

    def start(self, live_client_data: LiveClientData):
        value = self._get_stat(live_client_data)
        if value is None:
            return

        self._start_value = value
        self._current_value = value

        value = self._get_stat(live_client_data)
        if value is None:
            return

        self._start_value = value
        self._current_value = value

    def _on_update(self, dt: float, live_client_data: LiveClientData):
        self._current_value = self._get_stat(live_client_data)

    def _get_stat(self, live_client_data: LiveClientData):
        return live_client_data.get_field("activePlayer", "championStats", self._key)


