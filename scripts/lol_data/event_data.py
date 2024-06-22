"""
This module contains the EventData class.
"""

from .get_live_client_data import GetLiveClientData


class EventData:
    """
    This class contains the event data.
    """

    @classmethod
    def get_data(cls):
        return GetLiveClientData.all_data["events"]["Events"]

    @classmethod
    def get_event(cls, name: str):
        all_events = cls.get_data()
        events = []
        for event in all_events:
            if event["EventName"] == name:
                events.append(event)

        return events
