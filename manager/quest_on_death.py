import threading
import time

from .quest_frame_manager import QuestFrameManager
from ..lol_data.active_player_data import AcitvePlayerData


class QuestOnDeath:

    @classmethod
    def start(cls):
        cls.last_death_cont = AcitvePlayerData.get_death_count()

        cls.terminate_flag = False
        cls.receive_loop_thread = threading.Thread(target=cls.receive_loop)
        cls.receive_loop_thread.start()

    @classmethod
    def stop(cls):
        cls.terminate_flag = True
        cls.receive_loop_thread.join()

    @classmethod
    def receive_loop(cls):
        while not cls.terminate_flag:
            death_cont = AcitvePlayerData.get_death_count()

            if cls.last_death_cont < death_cont:
                QuestFrameManager.create_quest_frame_amount += 1
                cls.last_death_cont = death_cont

            time.sleep(0.2)
