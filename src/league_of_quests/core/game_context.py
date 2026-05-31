class GameContext:
    def __init__(self, live_client_data, live_client_config):
        self._live_client_data = live_client_data
        self._live_client_config = live_client_config

    def get_live_client_data(self):
        return self._live_client_data

    def get_live_client_config(self):
        return self._live_client_config
