from .cover_frame_base import CoverFrameBase
from ...utils.game_overlay_scaling import get_global_size, get_global_pos


class MultiCoverFrameBase(CoverFrameBase):
    def __init__(self, parent, cover_num):
        super().__init__(parent)
        self.cover_num = cover_num

    def setgeometry(
        self,
        min_size,
        max_size,
        min_space,
        max_space,
        min_x,
        max_x,
        min_y,
        max_y,
    ):
        size = get_global_size(min_size, max_size)
        space = get_global_size(min_space, max_space)
        x, y = get_global_pos(min_x, max_x, min_y, max_y)
        x += (size + space) * self.cover_num

        self.setGeometry(x, y, size, size)
