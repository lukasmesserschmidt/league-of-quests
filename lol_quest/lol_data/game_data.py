from .get_live_client_data import GetLiveClientData


class GameData:
    @classmethod
    def get_data(cls):
        return GetLiveClientData.all_data["gameData"]

    @classmethod
    def get_game_mode(cls):
        return cls.get_data()["gameMode"]
