from PySide6.QtCore import QTimer
import threading
import time

from .quest_frame_creator import QuestFrameCreator
from ..gui.quest_frame import QuestFrame
from ..gui.quest_display import quest_display


class QuestFrameManager:
    active_quest_frames = []

    create_quest_frame_amount = 0
    quest_frames_available = True

    @classmethod
    def start(cls):
        cls.create_quest_frame_amount = 0

        cls.create_quest_frame_loop_timer = QTimer()
        cls.create_quest_frame_loop_timer.timeout.connect(cls.create_quest_frame_loop)
        cls.create_quest_frame_loop_timer.start(500)

        cls.terminate_flag = False
        cls.update_quest_frame_loop_thread = threading.Thread(
            target=cls.update_quest_frame_loop
        )
        cls.update_quest_frame_loop_thread.start()

    @classmethod
    def stop(cls):
        cls.create_quest_frame_loop_timer.deleteLater()

        cls.terminate_flag = True
        cls.update_quest_frame_loop_thread.join()

        while len(cls.active_quest_frames) > 0:
            quest_frame = cls.active_quest_frames[0]
            cls.delete_quest_frame(quest_frame)

    @classmethod
    def create_quest_frame_loop(cls):
        for _ in range(cls.create_quest_frame_amount):
            if len(cls.active_quest_frames) < 5:
                cls.create_quest_frame()
            cls.create_quest_frame_amount -= 1

    @classmethod
    def create_quest_frame(cls):
        quest_frame = QuestFrameCreator.get_quest_frame(cls.active_quest_frames)
        if quest_frame:
            quest_display.add_widget(quest_frame)
            cls.active_quest_frames.append(quest_frame)
        else:
            cls.quest_frames_available = False

    @classmethod
    def update_quest_frame_loop(cls):
        while not cls.terminate_flag:
            for quest_frame in cls.active_quest_frames:
                if quest_frame.quest.terminate_flag:
                    cls.delete_quest_frame(quest_frame)

            time.sleep(0.2)

    @classmethod
    def delete_quest_frame(cls, quest_frame: QuestFrame):
        quest_frame.quest.stop()
        quest_frame.restriction.stop()
        cls.active_quest_frames.remove(quest_frame)
        quest_frame.deleteLater()
