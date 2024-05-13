import threading
import time

from .quest_frame_manager import QuestFrameManager
from .settings_manager import Settings


class QuestAfterTime:

    @classmethod
    def start(cls):
        cls.time = Settings.get_quest_after_time("time")
        cls.end_time = time.time() + cls.time

        cls.terminate_flag = False
        cls.receive_loop_thread = threading.Thread(target=cls.receive_loop)
        cls.receive_loop_thread.start()

    @classmethod
    def stop(cls):
        cls.terminate_flag = True
        cls.receive_loop_thread.join()
        cls.remaining_time = 0

    @classmethod
    def receive_loop(cls):
        while not cls.terminate_flag:
            if cls.end_time <= time.time():
                QuestFrameManager.create_quest_frame_amount += 1
                cls.end_time = time.time() + cls.time

            cls.remaining_time = cls.end_time - time.time()

            time.sleep(0.2)
