from .get_live_client_data import GetLiveClientData
from .event_data import EventData


class GameData:
    @classmethod
    def get_data(cls):
        return GetLiveClientData.all_data["gameData"]

    @classmethod
    def get_game_time(cls):
        return cls.get_data()["gameTime"]

    @classmethod
    def get_lol_is_running(cls):
        if GetLiveClientData.all_data:
            _, end = EventData.get_start_end_event().values()

            if not end:
                return True

        return False
