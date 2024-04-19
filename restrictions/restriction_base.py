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
        cls.terminate_flag = False
        cls.on_loop_start()
        # cls.restriction_loop_timer = QTimer()
        # cls.restriction_loop_timer.timeout.connect(cls.restriction_loop)
        # cls.restriction_loop_timer.start(100)
        restriction_loop_thread = threading.Thread(
            target=cls.restriction_loop, daemon=True
        )
        restriction_loop_thread.start()

    @classmethod
    def restriction_loop(cls):
        while True:
            cls.restriction_content()

            if cls.terminate_flag:
                # cls.on_loop_end()
                # cls.restriction_loop_timer.deleteLater()
                break

    @classmethod
    def on_loop_start(cls):
        pass

    @classmethod
    def on_loop_end(cls):
        pass

    @classmethod
    def restriction_content(cls):
        raise NotImplementedError
