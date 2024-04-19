from .multi_cover_base import MultiCoverBase
from .resource_cover_frame import ResourceCoverFrame


class ResourceCover(MultiCoverBase):
    def __init__(self, parent):
        super().__init__(parent, ResourceCoverFrame, 2)

    def activate_cover(self, *args: tuple[int, float]):
        for i in args:
            self.abilities[i[0]].show(i[1])
