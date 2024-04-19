from .multi_cover_base import MultiCoverBase
from .summoner_spell_cover_frame import SummonerSpellCoverFrame


class SummonerSpellCover(MultiCoverBase):
    def __init__(self, parent):
        super().__init__(parent, SummonerSpellCoverFrame, 2)
