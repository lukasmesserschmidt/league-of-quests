from typing import Callable
from PySide6.QtWidgets import QFrame
import time

from ...lol_data.lol_window_data import LolWindowData


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
        if LolWindowData.lol_is_top:
            super().show()
            self.set_geometry()
        else:
            self.hide()

    def hide(self, *args):
        time.sleep(0.001)
        super().hide()
