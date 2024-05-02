from .get_live_client_data import GetLiveClientData


class EventData:
    @classmethod
    def get_data(cls):
        return GetLiveClientData.all_data.get("events", {}).get("Events")

    @classmethod
    def get_event(cls, name: str):
        if all_events := cls.get_data():
            events = []
            for event in all_events:
                if event["EventName"] == name:
                    events.append(event)

            return events
