import threading
import time

from ..manager.settings_manager import Settings


class QuestBase:
    title: str
    update_title = False
    difficulty: int
    attributes = []

    remaining_time = 0

    finish_color_enabled = False

    @classmethod
    def check_dependencies(cls):
        return True

    @classmethod
    def start(cls):
        cls.on_start()
        cls.terminate_flag = False
        cls.finish_color_enabled = False
        quest_loop_thread = threading.Thread(target=cls.quest_loop, daemon=True)
        quest_loop_thread.start()

    @classmethod
    def quest_loop(cls):
        end_time = cls.get_end_time()

        while time.time() < end_time:
            cls.remaining_time = end_time - time.time()
            if cls.quest_content():
                cls.terminate_flag = True

            if cls.terminate_flag:
                break

        cls.terminate_flag = True

        cls.on_end()

    @classmethod
    def get_end_time(cls, multiplier: float = 1, duration_only: bool = False):
        end_time = (0 if duration_only else time.time()) + Settings.all_settings[
            "quest_settings"
        ]["quest_duration"] * multiplier

        return end_time

    @classmethod
    def on_start(cls):
        pass

    @classmethod
    def quest_content(cls):
        raise NotImplementedError()

    @classmethod
    def on_end(cls):
        pass
