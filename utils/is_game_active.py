from ..lol_data.event_data import EventData


def is_game_active():
    try:
        if EventData.get_event("GameEnd"):
            return False
        elif EventData.get_event("GameStart"):
            return True
    except:
        return False
