"""
This module contains the Base class for all quest and restrictions.
"""

from PySide6.QtCore import QTimer


class QuestRestrictionBase:
    """
    This class is the base class for all quest and restrictions.
    """

    # init variables
    title: str
    difficulty: int
    attributes = []

    alternating_difficulties = None

    main_loop_timer = None

    # update loop interval in ms
    interval = 500

    # control
    @classmethod
    def check_dependencies(cls):
        """
        Checks if the quest or restriction is ready to start.
        """
        return True

    @classmethod
    def start(cls):
        """
        Starts the update loop timer.
        """
        cls.init()

        if cls.main_loop_timer is None:
            cls.main_loop_timer = QTimer()
            cls.main_loop_timer.timeout.connect(cls._update_loop)

        cls.main_loop_timer.start(cls.interval)

    @classmethod
    def stop(cls):
        """
        Stops the update loop timer and calls the on_end method.
        """
        cls.main_loop_timer.stop()
        cls.on_end()

    # quest/restriction
    @classmethod
    def init(cls):
        """
        Initializes the quest or restriction.
        """

    @classmethod
    def _update_loop(cls):
        pass

    @classmethod
    def on_end(cls):
        """
        Called when the quest or restriction is finished.
        """
