"""
This module contains the MultiCoverBase class and MultiCoverFrameBase class.,
"""

from .cover_frame_base import CoverFrameBase
from ...utils.game_overlay_scaling import get_global_size, get_global_pos


class MultiCoverBase:
    """
    Base class for multi cover classes.
    """

    def __init__(self, parent, cover, num_covers):
        self.covers = [cover(parent, i) for i in range(0, num_covers)]

    def show(self, *args: int):
        for arg in args:
            self.covers[arg].show()

    def hide(self, *args: int):
        for arg in args:
            self.covers[arg].hide()


class MultiCoverFrameBase(CoverFrameBase):
    """
    Base class for multi cover frame classes.
    """

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
