from .live_client_data import LiveClientData


class EventData:
    @classmethod
    def get_data(cls):
        return LiveClientData.request_data()["events"]["Events"]

    @classmethod
    def get_kill_events(cls):
        events = cls.get_data()
        kill_events = []
        for event in events:
            if event["EventName"] == "ChampionKill":
                kill_events.append(event)

        return kill_events
