from ...core import Difficulty
from ...core.restrictions import Restriction


class DisableBaseAbilityRestriction(Restriction):
    description = "Ability {ability} disabled."
    difficulty = Difficulty.MEDIUM
    tags = ["ability"]

    def __init__(self, ability: str):
        super().__init__()
        self.ability = ability
