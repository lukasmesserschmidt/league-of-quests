from .cover_frame_base import CoverFrameBase
from .. import app
from ...utils.game_overlay_scaling import get_map_size


class MapCover(CoverFrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_geometry = lambda: self.setgeometry()

        self.setStyleSheet("background-color: rgb(0, 0, 0);\n" "border-radius: 10px")

    def setgeometry(self):
        x, y = app.get_app().primaryScreen().size().toTuple()
        size = get_map_size()
        x -= size
        y -= size
        self.setGeometry(x, y, size, size)
