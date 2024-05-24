from PySide6.QtCore import QTimer

from .quest_frame_manager import QuestFrameManager
from ..lol_data.active_player_data import ActivePlayerData


class QuestOnDeath:
    receive_loop_timer = None

    @classmethod
    def start(cls):
        if cls.receive_loop_timer is None:
            cls.receive_loop_timer = QTimer()
            cls.receive_loop_timer.timeout.connect(cls.receive_loop)

        cls.last_death_cont = ActivePlayerData.get_deaths()
        cls.receive_loop_timer.start(200)

    @classmethod
    def stop(cls):
        if cls.receive_loop_timer is not None:
            cls.receive_loop_timer.stop()

    @classmethod
    def receive_loop(cls):
        death_cont = ActivePlayerData.get_deaths()

        if cls.last_death_cont < death_cont:
            QuestFrameManager.create_quest_frame_amount += 1
            cls.last_death_cont = death_cont
