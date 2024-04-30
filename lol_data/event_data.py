from .get_live_client_data import GetLiveClientData


class EventData:
    @classmethod
    def get_data(cls):
        return GetLiveClientData.all_data["events"]["Events"]

    @classmethod
    def get_event_by_name(cls, name: str):
        all_events = cls.get_data()
        events = []
        for event in all_events:
            if event["EventName"] == name:
                events.append(event)

        return events

    @classmethod
    def get_start_end_event(cls):
        start = cls.get_event_by_name("GameStart")
        end = cls.get_event_by_name("GameEnd")
        start_end = {"start": any(start), "end": any(end)}

        return start_end

    @classmethod
    def get_kill_events(cls):
        return cls.get_event_by_name("ChampionKill")
