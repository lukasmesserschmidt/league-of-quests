from PySide6.QtCore import QTimer

from .quest_frame_manager import QuestFrameManager
from .quest_on_death import QuestOnDeath
from .quest_after_time import QuestAfterTime
from .settings_manager import Settings
from ..gui.quest_display import get_quest_display
from ..utils.time import convert_time


class MainManager:

    @classmethod
    def start(cls):
        QuestFrameManager.start()

        if Settings.get_quest_on_death:
            QuestOnDeath.start()
        if Settings.get_quest_after_time()["ischecked"]:
            QuestAfterTime.start()

        cls.main_loop_timer = QTimer()
        cls.main_loop_timer.timeout.connect(cls.main_loop)
        cls.main_loop_timer.start(500)

    @classmethod
    def stop(cls):
        cls.main_loop_timer.deleteLater()

        if Settings.get_quest_on_death:
            QuestOnDeath.stop()
        if Settings.get_quest_after_time()["ischecked"]:
            QuestAfterTime.stop()

        QuestFrameManager.stop()

    @classmethod
    def main_loop(cls):
        cls.update_timer_text()
        cls.update_quest_count()

    @classmethod
    def update_timer_text(cls):
        if not QuestFrameManager.quest_frames_available:
            get_quest_display().set_timer_text("No Quest Available")
            QuestFrameManager.quest_frames_available = True
        elif len(QuestFrameManager.active_quest_frames) <= 5:
            if Settings.get_quest_after_time()["ischecked"]:
                get_quest_display().set_timer_text(
                    convert_time(QuestAfterTime.remaining_time)
                )
            else:
                get_quest_display().set_timer_text("Not Active")

        else:
            get_quest_display().set_timer_text("Max Quests")

    @classmethod
    def update_quest_count(cls):
        get_quest_display().set_quest_count(len(QuestFrameManager.active_quest_frames))
