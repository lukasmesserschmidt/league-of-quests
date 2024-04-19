from .multi_cover_frame_base import MultiCoverFrameBase


class AbilityCoverFrame(MultiCoverFrameBase):
    def __init__(self, parent, ability_num):
        super().__init__(parent, ability_num)
        self.set_geometry = lambda: self.setgeometry(
            80, 120, 8, 13, 1615, 1459, 1985, 1895
        )
