from .get_live_client_data import request_data


class EventData:
    @classmethod
    def get_data(cls):
        url = "https://127.0.0.1:2999/liveclientdata/eventdata"
        return request_data(url)["Events"]

    @classmethod
    def get_kill_events(cls):
        events = cls.get_data()
        kill_events = []
        for event in events:
            if event["EventName"] == "ChampionKill":
                kill_events.append(event)

        return kill_events
