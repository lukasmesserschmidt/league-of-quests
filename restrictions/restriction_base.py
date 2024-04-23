from PySide6.QtCore import QTimer
import threading


class RestrictionBase:
    title: str
    difficulty: int
    attributes = []

    @classmethod
    def check_dependencies(cls):
        return True

    @classmethod
    def start(cls):
        cls.on_start()
        cls.terminate_flag = False
        restriction_loop_thread = threading.Thread(
            target=cls.restriction_loop, daemon=True
        )
        restriction_loop_thread.start()

    @classmethod
    def restriction_loop(cls):
        while True:
            cls.restriction_content()

            if cls.terminate_flag:
                cls.on_end()
                break

    @classmethod
    def on_start(cls):
        pass

    @classmethod
    def restriction_content(cls):
        raise NotImplementedError

    @classmethod
    def on_end(cls):
        pass
