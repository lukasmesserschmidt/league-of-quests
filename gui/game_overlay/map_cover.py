from .cover_frame_base import CoverFrameBase
from ...lol_data.lol_settings import LolSettings
from ...lol_data.lol_window_data import LolWindowData
from ...utils.game_overlay_scaling import get_map_size


class MapCover(CoverFrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_geometry = lambda: self.setgeometry()

        self.setStyleSheet("background-color: rgb(0, 0, 0);\n" "border-radius: 10px")

    def setgeometry(self):
        size = get_map_size()
        x, y = LolWindowData.get_scaled_resolution()
        window_x, window_y = LolWindowData.get_scaled_pos()
        x = (
            (window_x + x - size)
            if not LolSettings.get_lol_setting("flip_map")
            else LolWindowData.get_scaled_pos()[0]
        )
        y = window_y + y - size

        self.setGeometry(x, y, size, size)
