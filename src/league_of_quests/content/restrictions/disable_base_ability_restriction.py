import random

from .base import Restriction
from ...data import Difficulty, HotkeyType
from ...game import GameContext


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
    def requirements_met(cls, game_context: GameContext):
        available_options = cls._get_available_options(game_context)
        return len(available_options) > 0

    def _on_start(self, game_context: GameContext):
        available_options = self.__class__._get_available_options(game_context)
        self.selected_option = random.choice(available_options)

        self._format_description(ability=self.options[self.selected_option])

    def activate(self):
        self._game_disruptor.disable_ability(self.selected_option, self.get_id())

    def deactivate(self):
        self._game_disruptor.enable_ability(self.selected_option, self.get_id())

    @classmethod
    def _get_available_options(cls, game_context: GameContext):
        live_client_config = game_context.get_config()
        return [
            option
            for option in cls.options.keys()
            if getattr(live_client_config.input, option.value)
        ]
