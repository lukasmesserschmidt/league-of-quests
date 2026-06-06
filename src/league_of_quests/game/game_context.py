from ..data import LiveClientData
from ..data import LiveClientConfig


class GameContext:
    def __init__(
        self, game_context: LiveClientData, live_client_config: LiveClientConfig
    ):
        self._live_client_data = game_context
        self._live_client_config = live_client_config

    def get_data(self) -> LiveClientData:
        return self._live_client_data

    def get_config(self) -> LiveClientConfig:
        return self._live_client_config
