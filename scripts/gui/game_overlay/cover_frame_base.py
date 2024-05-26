from typing import Callable
from PySide6.QtWidgets import QFrame


class CoverFrameBase(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_geometry: Callable
        self.setStyleSheet("background-color: rgba(70, 10, 10, 200)")

        self.hide()

    def setgeometry(self):
        raise NotImplementedError

    def show(self, *args):
        self.set_geometry()
        super().show()

    def hide(self, *args):
        super().hide()
