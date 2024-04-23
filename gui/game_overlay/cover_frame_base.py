from typing import Callable

from PySide6.QtWidgets import QFrame
from PySide6.QtCore import QTimer


class CoverFrameBase(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_geometry: Callable
        self.setStyleSheet(
            "background-color: rgba(70, 10, 10, 200);\n" "border-radius: 0px"
        )

        self.hide()

    def setgeometry(self):
        raise NotImplementedError

    def show(self, *args):
        super().show()
        self.set_geometry()

    def hide(self, *args):
        return super().hide()
