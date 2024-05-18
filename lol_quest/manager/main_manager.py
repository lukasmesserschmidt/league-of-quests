from contextlib import suppress

from .quest_display_manager import QuestDisplayManager
from .quest_frame_manager import QuestFrameManager
from .quest_on_death import QuestOnDeath
from .quest_after_time import QuestAfterTime
from .settings_manager import Settings


class MainManager:

    @classmethod
    def start(cls):
        QuestFrameManager.start()

        if Settings.get_quest_on_death():
            QuestOnDeath.start()
        if Settings.get_quest_after_time("ischecked"):
            QuestAfterTime.start()

        QuestDisplayManager.start()

    @classmethod
    def stop(cls):
        with suppress(Exception):
            QuestDisplayManager.stop()

        with suppress(Exception):
            QuestOnDeath.stop()
        with suppress(Exception):
            QuestAfterTime.stop()

        with suppress(Exception):
            QuestFrameManager.stop()
