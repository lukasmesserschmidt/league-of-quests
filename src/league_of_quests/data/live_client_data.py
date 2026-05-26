class LiveClientData:
    def __init__(self, data: dict | None):
        self.data = data

    def get_ability_power(self) -> float | None:
        return self.get_field("activePlayer", "championStats", "abilityPower")

    def get_game_time(self) -> float | None:
        return self.get_field("gameData", "gameTime")

    def get_field(self, *path: str, default=None) -> Any:
        node = self.data
        for key in path:
            if not isinstance(node, Mapping):
                return default
            node = node.get(key, default)
            if node is default:
                return default
        return node
