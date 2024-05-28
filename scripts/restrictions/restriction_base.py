from PySide6.QtCore import QTimer


class RestrictionBase:
    title: str
    difficulty: int
    attributes = []

    restriction_loop_timer = None
    interval = 500

    # control
    @classmethod
    def check_dependencies(cls):
        return True

    @classmethod
    def start(cls):
        cls.init()

        if cls.restriction_loop_timer is None:
            cls.restriction_loop_timer = QTimer()
            cls.restriction_loop_timer.timeout.connect(cls.restriction_content)

        cls.restriction_loop_timer.start(cls.interval)

    @classmethod
    def stop(cls):
        cls.restriction_loop_timer.stop()
        cls.on_end()

    # restriction
    @classmethod
    def init(cls):
        pass

    @classmethod
    def restriction_content(cls):
        raise NotImplementedError

    @classmethod
    def on_end(cls):
        pass
