from .restriction_base import RestrictionBase
from ..gui.game_overlay.game_overlay_window import get_game_overlay


class CoverMap(RestrictionBase):
    title = "Map covered!"
    difficulty = 2

    @classmethod
    def restriction_content(cls):
        get_game_overlay().map_cover.show()

    @classmethod
    def on_end(cls):
        get_game_overlay().map_cover.hide()
