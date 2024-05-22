from .cover_frame_base import CoverFrameBase
from ...utils.game_overlay_scaling import get_global_pos, get_global_size


class SingleCoverBase(CoverFrameBase):
    def __init__(self, parent):
        super().__init__(parent)

    def setgeometry(self, min_size, max_size, min_x, max_x, min_y, max_y):
        size = get_global_size(min_size, max_size)
        x, y = get_global_pos(min_x, max_x, min_y, max_y)

        self.setGeometry(x, y, size, size)
