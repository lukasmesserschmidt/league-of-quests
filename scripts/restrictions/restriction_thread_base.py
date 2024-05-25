import threading
import time

from .restriction_base import RestrictionBase


class RestrictionThreadBase(RestrictionBase):
    terminate_flag = False

    # control
    @classmethod
    def start(cls):
        cls.terminate_flag = False

        cls.init()

        cls.restriction_loop_thread = threading.Thread(target=cls._restriction_loop)
        cls.restriction_loop_thread.start()

    @classmethod
    def stop(cls):
        cls.terminate_flag = True
        cls.restriction_loop_thread.join()
        cls.on_end()

    # restriction
    @classmethod
    def _restriction_loop(cls):
        while not cls.terminate_flag:
            cls.restriction_content()

            cls.wait_interval()

    # utils
    @classmethod
    def wait_interval(cls):
        end_time = time.time() + cls.interval
        while time.time() < end_time and not cls.terminate_flag:
            time.sleep(0.01)
