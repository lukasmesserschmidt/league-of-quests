from .multi_cover_base import MultiCoverBase, MultiCoverFrameBase
from ...utils.game_overlay_scaling import get_global_size, get_global_pos


class ResourceCover(MultiCoverBase):
    def __init__(self, parent):
        super().__init__(parent, ResourceCoverFrame, 2)


class ResourceCoverFrame(MultiCoverFrameBase):
    def __init__(self, parent, cover_num):
        super().__init__(parent, cover_num)
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
        x, y = get_global_pos(min_x, max_x, min_y, max_y)
        y += (y_size + space) * self.cover_num

        x_size *= self.percent

        self.setGeometry(x, y, x_size, y_size)

    def update_cover(self, enable: tuple[bool, float]):
        self.percent = enable[1]
        super().update_cover(*enable)
