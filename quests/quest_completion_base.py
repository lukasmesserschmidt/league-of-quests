from .quest_base import QuestBase
import time


class QuestCompletionBase(QuestBase):
    completion_duration = 20
    remaining_quest_time = 0

    @classmethod
    def quest_loop(cls):
        cls.on_start()
        end_time = cls.get_end_time()

        while time.time() < end_time:
            cls.remaining_quest_time = end_time - time.time()
            cls.remaining_time = cls.remaining_quest_time
            if cls.quest_content():
                cls.completion_loop()
                end_time = time.time() + cls.remaining_quest_time

            if cls.terminate_flag:
                break

        cls.on_end()
        cls.terminate_flag = True

    @classmethod
    def completion_loop(cls):
        cls.finish_color_enabled = True

        end_time = time.time() + cls.completion_duration
        while time.time() < end_time:
            cls.remaining_time = end_time - time.time()
            if cls.quest_content() == None:
                cls.finish_color_enabled = False
                break

            if cls.terminate_flag:
                break
        else:
            cls.terminate_flag = True
