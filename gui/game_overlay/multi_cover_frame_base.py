from PySide6.QtWidgets import QFrame

from .cover_frame_base import CoverFrameBase
from ...utils.game_overlay_scaling import get_global_size, get_scaled_pos


class MultiCoverFrameBase(CoverFrameBase):
    def __init__(self, parent, ability_num):
        super().__init__(parent)
        self.ability_num = ability_num

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
        x, y = get_scaled_pos(min_x, max_x, min_y, max_y)
        x += (size + space) * self.ability_num

        self.setGeometry(x, y, size, size)
