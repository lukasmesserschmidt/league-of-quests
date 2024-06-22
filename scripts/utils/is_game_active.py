"""
This module contains functions for checking if the game is active.
"""

from contextlib import suppress

from ..lol_data.event_data import EventData
from ..lol_data.get_lol_settings import GetLolSettings
from ..lol_data.lol_window_data import LolWindowData


def is_game_active():
    """
    Returns if the game is active, based on: game started and not ended, lol is open,
      all lol settings are available and the game cfg is available.
    """
    with suppress(Exception):
        if EventData.get_event("GameEnd"):
            return False
        elif (
            LolWindowData.is_lol_open()
            and EventData.get_event("GameStart")
            and GetLolSettings.all_lol_settings is not None
            and GetLolSettings.game_cfg is not None
        ):
            return True
    return False
