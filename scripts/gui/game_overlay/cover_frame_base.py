from typing import Callable
from PySide6.QtWidgets import QFrame, QWidget

from ...utils.game_overlay_scaling import get_global_pos, get_global_size


class CoverFrameBase(QFrame):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.set_geometry: Callable
        self.setStyleSheet("background-color: rgba(70, 10, 10, 200)")

        self.hide()

    def setgeometry(self, min_size, max_size, min_x, max_x, min_y, max_y):
        size = get_global_size(min_size, max_size)
        x, y = get_global_pos(min_x, max_x, min_y, max_y)

        self.setGeometry(x, y, size, size)

    def show(self, *args):
        self.set_geometry()
        super().show()

    def hide(self, *args):
        super().hide()
