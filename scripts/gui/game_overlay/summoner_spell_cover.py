from .multi_cover_base import MultiCoverBase, MultiCoverFrameBase


class SummonerSpellCover(MultiCoverBase):
    def __init__(self, parent):
        super().__init__(parent, SummonerSpellCoverFrame, 2)


class SummonerSpellCoverFrame(MultiCoverFrameBase):
    def __init__(self, parent, cover_num):
        super().__init__(parent, cover_num)
        self.set_geometry = lambda: self.setgeometry(
            59, 90, 7, 12, 1979, 2008, 1986, 1895
        )
