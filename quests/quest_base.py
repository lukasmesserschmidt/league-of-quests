import threading
import time

from ..manager.settings_manager import Settings


class QuestBase:
    title: str
    difficulty: int
    attributes = []

    remaining_time = 0

    finish_color_enabled = False

    @classmethod
    def check_dependencies(cls):
        return True

    @classmethod
    def start(cls):
        cls.terminate_flag = False
        cls.finish_color_enabled = False
        quest_loop_thread = threading.Thread(target=cls.quest_loop, daemon=True)
        quest_loop_thread.start()

    @classmethod
    def quest_loop(cls):
        cls.on_quest_start()
        end_time = (
            time.time() + Settings.all_settings["quest_settings"]["quest_duration"]
        )

        while time.time() < end_time:
            cls.remaining_time = end_time - time.time()
            if cls.quest_content():
                cls.terminate_flag = True

            if cls.terminate_flag:
                break

        cls.terminate_flag = True

    @classmethod
    def on_quest_start(cls):
        pass

    @classmethod
    def quest_content(cls):
        raise NotImplementedError()
