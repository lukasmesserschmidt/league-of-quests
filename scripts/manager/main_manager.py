import keyboard

from .quest_display_manager import QuestDisplayManager
from .quest_frame_manager import QuestFrameManager
from .quest_on_death import QuestOnDeath
from .quest_after_time import QuestAfterTime
from .settings_manager import SettingsManager
from ..lol_data.lol_window_data import LolWindowData
from ..lol_data.get_live_client_data import GetLiveClientData
from ..lol_data.get_lol_settings import GetLolSettings
from ..gui.quest_display import get_quest_display
from ..gui.stop_window import get_stop_window
from ..gui.game_overlay.game_overlay_window import get_game_overlay
from ..utils import is_program_active


class MainManager:

    @classmethod
    def start_game(cls):
        LolWindowData.start()

        QuestFrameManager.start()

        if SettingsManager.get_quest_on_death():
            QuestOnDeath.start()
        if SettingsManager.get_quest_after_time("ischecked"):
            QuestAfterTime.start()

        QuestDisplayManager.start()
        get_quest_display().start()
        get_game_overlay().start()

        get_stop_window().start()

        is_program_active.program_active = True

    @classmethod
    def stop_game(cls):
        get_stop_window().stop()

        get_game_overlay().stop()
        get_quest_display().stop()
        QuestDisplayManager.stop()

        QuestAfterTime.stop()
        QuestOnDeath.stop()

        QuestFrameManager.stop()

        LolWindowData.stop()
        GetLiveClientData.all_data = None

        is_program_active.program_active = False

        keyboard.unhook_all()

    @classmethod
    def stop_program(cls):
        cls.stop_game()

        GetLolSettings.stop()
        GetLiveClientData.stop()
