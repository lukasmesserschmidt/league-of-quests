from .restriction_base import RestrictionBase
from ..common_classes.enable_overlay_base import EnableOverlayBase
from ..gui.game_overlay.game_overlay_window import GameOverlayWindow
from ..utils.constants import Constants


class CoverMap(RestrictionBase, EnableOverlayBase):
    title = "Map covered!"
    difficulty = 2
    attributes = [Constants.MAP]

    overlay_types = {Constants.MAP: [0]}

    @classmethod
    def restriction_content(cls):
        cls.enable_overlays(True)

    @classmethod
    def on_end(cls):
        cls.enable_overlays(False)
