import threading
import time

from ..manager.settings_manager import Settings


class QuestBase:
    title: str
    difficulty: int
    attributes: list

    duration = 0
    remaining_time = 0

    terminate_flag: bool
    interval = 0.2
    update_title = False
    finish_color_enabled = False

    # control
    @classmethod
    def check_dependencies(cls):
        return True

    @classmethod
    def start(cls):
        cls.terminate_flag = False
        cls.finish_color_enabled = False

        cls.init()

        cls.quest_loop_thread = threading.Thread(target=cls._quest_main)
        cls.quest_loop_thread.start()

    @classmethod
    def stop(cls):
        cls.terminate_flag = True
        cls.quest_loop_thread.join()
        cls.remaining_time = 0

    # quest
    @classmethod
    def init(cls):
        cls.duration = cls.get_duration()

    @classmethod
    def _quest_main(cls):
        cls.quest_loop_container()

        cls.on_end()
        cls.terminate_flag = True

    @classmethod
    def quest_loop_container(cls):
        cls._quest_loop()

    @classmethod
    def _quest_loop(cls):
        cls.end_time = cls.get_end_time(cls.duration)

        while time.time() < cls.end_time and not cls.terminate_flag:
            cls.quest_content_container()

            if not cls.terminate_flag:
                time.sleep(cls.interval)

    @classmethod
    def quest_content_container(cls):
        cls.remaining_time = cls.get_remaining_time(cls.end_time)
        cls.quest_content()

    @classmethod
    def quest_content(cls):
        raise NotImplementedError

    @classmethod
    def on_end(cls):
        pass

    # utils
    @classmethod
    def get_duration(cls, multiplier: float = 1):
        return Settings.get_quest_duration() * multiplier

    @classmethod
    def get_end_time(cls, duration):
        return time.time() + duration

    @classmethod
    def get_remaining_time(cls, end_time):
        return end_time - time.time()
