from .quest_base import QuestBase
import time

from ..manager.settings_manager import Settings


class QuestCompletionBase(QuestBase):
    completion_duration = 20
    remaining_quest_time = 0

    @classmethod
    def quest_loop(cls):
        cls.on_quest_start()
        end_time = (
            time.time() + Settings.all_settings["quest_settings"]["quest_duration"]
        )

        while time.time() < end_time:
            cls.remaining_quest_time = end_time - time.time()
            cls.remaining_time = cls.remaining_quest_time
            if cls.quest_content():
                cls.completion_loop()
                end_time = time.time() + cls.remaining_quest_time

            if cls.terminate_flag:
                break

        cls.terminate_flag = True

    @classmethod
    def completion_loop(cls):
        cls.finish_color_enabled = True

        end_time = time.time() + cls.completion_duration
        while time.time() < end_time:
            cls.remaining_time = end_time - time.time()
            if cls.quest_content() == False:
                cls.finish_color_enabled = False
                break
        else:
            cls.terminate_flag = True
