from contextlib import suppress
from ..lol_data.event_data import EventData


def is_game_active():
    if EventData.get_event("GameEnd"):
        return False
    else:
        return bool(EventData.get_event("GameStart"))
        try:
            return bool(EventData.get_event("GameStart"))
        except:
            return False
