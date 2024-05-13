from .multi_cover_base import MultiCoverBase
from .ability_cover_frame import AbilityCoverFrame


class AbilityCover(MultiCoverBase):
    def __init__(self, parent):
        super().__init__(parent, AbilityCoverFrame, 4)
