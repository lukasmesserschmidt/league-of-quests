from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal


class WindowBase(QWidget):
    closed = Signal()

    def __init__(self):
        super().__init__()

    def closeEvent(self, event: QCloseEvent):
        self.hide()
        self.closed.emit()
        super().closeEvent(event)
