from PySide6.QtWidgets import QWidget, QFrame
from PySide6.QtCore import Qt

from .map_cover import MapCover
from .ability_cover import AbilityCover
from .summoner_spell_cover import SummonerSpellCover
from .resource_cover import ResourceCover
from .trinket_cover import TrinketCover
from .teleport_cover import TeleportCover
from .. import app


class GameOverlay(QWidget):
    def __init__(self):
        super().__init__()
        width, height = app.app.primaryScreen().size().toTuple()
        self.setGeometry(0, 0, width, height)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint
            | Qt.WindowTransparentForInput
            | Qt.FramelessWindowHint
        )

        self.show()

        self.ability_cover = AbilityCover(self)
        self.summoner_spell_cover = SummonerSpellCover(self)
        self.map_cover = MapCover(self)
        self.trinket_cover = TrinketCover(self)
        self.teleport_cover = TeleportCover(self)

        self.resource_cover = ResourceCover(self)

    def disable_cover(self, disable: bool, overlay_type: str, *args: int):
        overlay_type = getattr(self, f"{overlay_type}_cover")
        if disable:
            overlay_type.hide(*args)
        else:
            overlay_type.show(*args)


game_overlay = GameOverlay()


def create_window():
    global game_overlay
    game_overlay = GameOverlay()
