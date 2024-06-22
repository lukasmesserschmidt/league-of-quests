"""
This module contains the QuestOnDeath class.
"""

from PySide6.QtCore import QTimer

from .quest_frame_manager import QuestFrameManager
from ..lol_data.active_player_data import ActivePlayerData


class QuestOnDeath:
    """
    A class for managing the quest on death option.
    """

    # init variables
    _receive_loop_timer = None

    @classmethod
    def start(cls):
        """
        Start the receive loop timer.
        """
        if cls._receive_loop_timer is None:
            cls._receive_loop_timer = QTimer()
            cls._receive_loop_timer.timeout.connect(cls._receive_loop)

        cls.last_death_cont = ActivePlayerData.get_deaths()
        cls._receive_loop_timer.start(500)

    @classmethod
    def stop(cls):
        """
        Stop the receive loop timer.
        """
        if cls._receive_loop_timer is not None:
            cls._receive_loop_timer.stop()

    @classmethod
    def _receive_loop(cls):
        death_cont = ActivePlayerData.get_deaths()

        if cls.last_death_cont < death_cont:
            QuestFrameManager.create_quest_frame_amount += 1
            cls.last_death_cont = death_cont
