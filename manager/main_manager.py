from PySide6.QtCore import QTimer, QThread
import threading
import time

from .quest_frame_manager import QuestFrameManager
from .quest_on_death import QuestOnDeath
from .quest_after_time import QuestAfterTime
from .settings_manager import Settings
from ..gui.quest_display import quest_display
from ..utils.time import convert_time


class MainManager:

    @classmethod
    def start(cls):
        QuestFrameManager.start()

        cls.start_receivers()

        cls.terminate_flag = False
        cls.main_loop_thread = threading.Thread(target=cls.main_loop)
        cls.main_loop_thread.start()

    @classmethod
    def start_receivers(cls):
        if Settings.get_quest_on_death:
            QuestOnDeath.start()
        if Settings.get_quest_after_time()["ischecked"]:
            QuestAfterTime.start()

    @classmethod
    def stop(cls):
        cls.terminate_flag = True
        cls.main_loop_thread.join()

        if Settings.get_quest_on_death:
            QuestOnDeath.stop()
        if Settings.get_quest_after_time()["ischecked"]:
            QuestAfterTime.stop()

        QuestFrameManager.stop()

    @classmethod
    def main_loop(cls):
        while not cls.terminate_flag:
            cls.update_timer_text()
            cls.update_quest_count()

    @classmethod
    def update_timer_text(cls):
        if not QuestFrameManager.quest_frames_available:
            quest_display.set_timer_text("No Quest Available")
            time.sleep(3)
            QuestFrameManager.quest_frames_available = True
        elif len(QuestFrameManager.active_quest_frames) <= 5:
            if Settings.get_quest_after_time()["ischecked"]:
                quest_display.set_timer_text(
                    convert_time(QuestAfterTime.remaining_time)
                )
            else:
                quest_display.set_timer_text("Not Active")

        else:
            quest_display.set_timer_text("Max Quests")

    @classmethod
    def update_quest_count(cls):
        quest_display.set_quest_count(len(QuestFrameManager.active_quest_frames))
