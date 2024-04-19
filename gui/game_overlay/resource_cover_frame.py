from PySide6.QtWidgets import QFrame

from .multi_cover_frame_base import MultiCoverFrameBase
from ...utils.game_overlay_scaling import get_global_size, get_scaled_pos


class ResourceCoverFrame(MultiCoverFrameBase):
    def __init__(self, parent, ability_num):
        super().__init__(parent, ability_num)
        self.set_geometry = lambda: self.setgeometry(
            548, 828, 23, 35, 3, 5, 1553, 1364, 2093, 2058
        )

        self.percent = 1

    def setgeometry(
        self,
        min_x_size,
        max_x_size,
        min_y_size,
        max_y_size,
        min_space,
        max_space,
        min_x,
        max_x,
        min_y,
        max_y,
    ):
        x_size, y_size = get_global_size(min_x_size, max_x_size), get_global_size(
            min_y_size, max_y_size
        )
        space = get_global_size(min_space, max_space)
        x, y = get_scaled_pos(min_x, max_x, min_y, max_y)
        y += (y_size + space) * self.ability_num

        x_size *= self.percent

        self.setGeometry(x, y, x_size, y_size)

    def show(self, percent):
        super().show()
        self.percent = percent
