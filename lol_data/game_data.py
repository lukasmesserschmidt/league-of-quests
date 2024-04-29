from .live_client_data import LiveClientData


class GameData:
    @classmethod
    def get_data(cls):
        return LiveClientData.all_data["gameData"]

    @classmethod
    def get_game_time(cls):
        return cls.get_data()["gameTime"]
