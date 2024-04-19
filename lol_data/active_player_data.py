from .live_client_data import request_data
from .event_data import EventData


class AcitvePlayerData:
    @classmethod
    def get_data(cls):
        url = "https://127.0.0.1:2999/liveclientdata/activeplayer"
        return request_data(url)

    @classmethod
    def get_summoner_name(cls):
        url = "https://127.0.0.1:2999/liveclientdata/activeplayername"
        return request_data(url).split("#")[0]

    @classmethod
    def get_current_gold(cls):
        return cls.get_data()["currentGold"]

    @classmethod
    def get_death_count(cls):
        events = EventData.get_kill_events()
        death_count = 0

        for event in events:
            if event["VictimName"] == cls.get_summoner_name():
                death_count += 1

        return death_count
