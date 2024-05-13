from .get_live_client_data import GetLiveClientData
from .event_data import EventData


class GameData:
    @classmethod
    def get_data(cls):
        return GetLiveClientData.all_data["gameData"]

    @classmethod
    def get_game_time(cls):
        return cls.get_data()["gameTime"]
