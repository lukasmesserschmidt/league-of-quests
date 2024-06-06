from PySide6.QtCore import QTimer


class QuestRestrictionBase:
    title: str
    difficulty: int
    attributes = []

    alternating_difficulties = None

    main_loop_timer = None
    interval = 300

    # control
    @classmethod
    def check_dependencies(cls):
        return True

    @classmethod
    def start(cls):
        cls.init()

        if cls.main_loop_timer is None:
            cls.main_loop_timer = QTimer()
            cls.main_loop_timer.timeout.connect(cls._main_loop)

        cls.main_loop_timer.start(cls.interval)

    @classmethod
    def stop(cls):
        cls.main_loop_timer.stop()
        cls.on_end()

    # quest/restriction
    @classmethod
    def init(cls):
        pass

    @classmethod
    def _main_loop(cls):
        pass

    @classmethod
    def on_end(cls):
        pass
