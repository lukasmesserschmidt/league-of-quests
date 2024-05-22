from ..lol_data.event_data import EventData
from ..lol_data.get_lol_settings import GetLolSettings


def is_game_active():
    try:
        if EventData.get_event("GameEnd"):
            return False
        elif (
            EventData.get_event("GameStart")
            and GetLolSettings.all_lol_settings is not None
            and GetLolSettings.game_cfg is not None
        ):
            return True
    except:
        return False
