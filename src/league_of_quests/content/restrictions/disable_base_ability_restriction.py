import random

from ...core import Difficulty
from ...core.restrictions import Restriction
from ...core.enums import HotkeyType


class DisableBaseAbilityRestriction(Restriction):
    description = "Ability {ability} disabled."
    difficulty = Difficulty.MEDIUM
    tags = ["ability"]

    options = {
        HotkeyType.ABILITY_1: "1",
        HotkeyType.ABILITY_2: "2",
        HotkeyType.ABILITY_3: "3",
    }

    @classmethod
    def requirements_met(cls, live_client_data, live_client_config):
        available_options = cls._get_available_options(live_client_config)
        return len(available_options) > 0

    def _on_start(self, live_client_data):
        available_options = self._get_available_options(self.live_client_config)
        self.selected_option = random.choice(available_options)

        self.description = self.description.format(
            ability=f"ability {self.options[self.selected_option]}"
        )

    def activate(self):
        self._game_disruptor.disable_ability(self.selected_option)

    def deactivate(self):
        self._game_disruptor.enable_ability(self.selected_option)

    def _get_available_options(self, live_client_config):
        return [
            option
            for option in self.options.keys()
            if getattr(live_client_config.input, option.value)
        ]
