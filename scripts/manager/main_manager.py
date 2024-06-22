"""
This module contains the MainManager class, which manages the main components of the program.
"""

import keyboard

from .quest_display_manager import QuestDisplayManager
from .quest_frame_manager import QuestFrameManager
from .quest_on_death import QuestOnDeath
from .quest_after_time import QuestAfterTime
from .settings_manager import SettingsManager
from .hotkey_manager import HotkeyManager
from ..lol_data.lol_window_data import LolWindowData
from ..lol_data.get_live_client_data import GetLiveClientData
from ..lol_data.get_lol_settings import GetLolSettings
from ..gui.quest_display import QuestDisplay
from ..gui.stop_window import StopWindow
from ..gui.game_overlay.game_overlay_window import GameOverlayWindow
from ..utils import is_program_active


class MainManager:
    """
    A class for managing the main components of the program.
    """

    @classmethod
    def start_game(cls):
        """
        Starts the game by invoking start methods for various components.
        """
        LolWindowData.start()

        QuestFrameManager.start()

        if SettingsManager.get_quest_on_death():
            QuestOnDeath.start()
        if SettingsManager.get_quest_after_time():
            QuestAfterTime.start()

        HotkeyManager.start()

        QuestDisplayManager.start()
        QuestDisplay.get_instance().start()
        GameOverlayWindow.get_instance().start()

        StopWindow.get_instance().start()

        is_program_active.program_active = True

    @classmethod
    def stop_game(cls):
        """
        Stops the game by invoking stop methods for various components and resetting program state.
        """
        StopWindow.get_instance().stop()

        GameOverlayWindow.get_instance().stop()
        QuestDisplay.get_instance().stop()
        QuestDisplayManager.stop()

        HotkeyManager.stop()

        QuestAfterTime.stop()
        QuestOnDeath.stop()

        QuestFrameManager.stop()

        LolWindowData.stop()
        GetLiveClientData.all_data = None

        is_program_active.program_active = False

        keyboard.unhook_all()

    @classmethod
    def stop_program(cls):
        """
        Stops the program by invoking the stop methods for the game
        and the data retrieval components.
        """
        cls.stop_game()

        GetLolSettings.stop()
        GetLiveClientData.stop()
