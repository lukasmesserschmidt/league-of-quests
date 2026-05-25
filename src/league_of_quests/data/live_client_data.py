from typing import Any, Mapping, Optional


class LiveClientData:
    """Small wrapper around the liveclient JSON payload for convenient access."""

    def __init__(self, data: Optional[Mapping[str, Any]]):
        self.data = data

    def get_ability_power(self) -> Optional[float]:
        return self._get_field("activePlayer", "championStats", "abilityPower")

    def get_game_time(self) -> Optional[float]:
        return self._get_field("gameData", "gameTime")

    def _get_field(self, *path, default: Any = None) -> Any:
        """Safely get a nested field from the payload.

        Example: `get_field('activePlayer', 'championStats', 'abilityPower')`
        """
        node = self.data
        for key in path:
            if not isinstance(node, Mapping):
                return default
            node = node.get(key, default)
            if node is default:
                return default
        return node
