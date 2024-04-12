from PySide6.QtWidgets import QWidget, QFrame
from PySide6.QtCore import Qt

from .. import app
from .map_cover import MapCover


class GameOverlay(QWidget):
    def __init__(self):
        super().__init__()
        width, height = app.app.primaryScreen().size().toTuple()
        self.setGeometry(0, 0, width, height)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint
            | Qt.WindowTransparentForInput
            | Qt.FramelessWindowHint
        )

        map_cover = MapCover(self)
        map_cover.show()
