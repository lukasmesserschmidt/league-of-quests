from PySide6.QtWidgets import QFrame

from .. import app
from ...lol_data.lol_settings import LolSettings


class MapCover(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("background-color: rgb(0, 0, 0);\n" "border-radius: 10px")

    def show(self):
        x, y = app.app.primaryScreen().size().toTuple()
        max_size = 800 / 3840 * x
        min_size = 400 / 3840 * x
        scale = ((max_size - min_size) / 3) * LolSettings.get_map_scale() + min_size
        x -= scale
        y -= scale
        self.setGeometry(x, y, scale, scale)

        super().show()
