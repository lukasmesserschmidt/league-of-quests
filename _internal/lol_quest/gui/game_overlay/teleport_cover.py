from .single_cover_base import SingleCoverBase


class TeleportCover(SingleCoverBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_geometry = lambda: self.setgeometry(53, 80, 2339, 2555, 2053, 1996)
