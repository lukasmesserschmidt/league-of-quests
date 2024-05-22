from .multi_cover_base import MultiCoverBase
from .resource_cover_frame import ResourceCoverFrame


class ResourceCover(MultiCoverBase):
    def __init__(self, parent):
        super().__init__(parent, ResourceCoverFrame, 2)

    def show(self, *args: tuple[int, float]):
        for arg in args:
            self.covers[arg[0]].show(arg[1])

    def hide(self, *args: tuple[int, float]):
        for arg in args:
            self.covers[arg[0]].hide(arg[1])
