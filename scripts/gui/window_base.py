"""
This module contains the WindowBase class.
"""

from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal


class WindowBase(QWidget):
    """
    A base class for most windows in the program.
    """

    _instances = {}

    closed = Signal()

    @classmethod
    def get_instance(cls, *args, **kwargs):
        """
        Returns an instance of the class, creating it if necessary.
        """

        if cls not in cls._instances:
            cls._instances[cls] = cls(*args, **kwargs)

        return cls._instances[cls]

    def closeEvent(self, event: QCloseEvent):
        self.hide()
        self.closed.emit()
        super().closeEvent(event)
