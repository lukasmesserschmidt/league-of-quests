from .restriction_base import RestrictionBase
from ..gui.game_overlay.game_overlay_window import get_game_overlay
from ..utils.constants import Constants


class CoverMap(RestrictionBase):
    title = "Map covered!"
    difficulty = 2
    attributes = [Constants.MAP]

    overlay_types = {Constants.MAP: [0]}

    @classmethod
    def restriction_content(cls):
        get_game_overlay().enable_cover(True, cls.overlay_types)

    @classmethod
    def on_end(cls):
        get_game_overlay().enable_cover(False, cls.overlay_types)
