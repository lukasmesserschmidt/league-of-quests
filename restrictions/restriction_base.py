import threading
import time


class RestrictionBase:
    title: str
    difficulty: int
    attributes = []

    terminate_flag: bool

    # control
    @classmethod
    def check_dependencies(cls):
        return True

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

    # restriction
    @classmethod
    def init(cls):
        pass

    @classmethod
    def _restriction_loop(cls):
        while not cls.terminate_flag:
            cls.restriction_content()

            time.sleep(0.2)

        cls.on_end()

    @classmethod
    def restriction_content(cls):
        raise NotImplementedError

    @classmethod
    def on_end(cls):
        pass
