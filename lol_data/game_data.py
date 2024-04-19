from .live_client_data import request_data


class GameData:
    @classmethod
    def get_data(cls):
        url = "https://127.0.0.1:2999/liveclientdata/gamestats"
        return request_data(url)

    @classmethod
    def get_game_time(cls):
        return cls.get_data()["gameTime"]
