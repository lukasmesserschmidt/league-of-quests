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
        self.resource_cover = ResourceCover(self)
        self.map_cover = MapCover(self)
        self.trinket_cover = TrinketCover(self)
        self.teleport_cover = TeleportCover(self)

        # self.abilitey_cover.activate_cover(0, 1, 2, 3)
        # self.summoner_spell_cover.activate_cover(0, 1)
        # self.resource_cover.activate_cover((0, 0.3), (1, 0.5))
        # self.map_cover.show()
        # self.trinket_cover.show()
        # self.teleport_cover.show()


game_overlay = GameOverlay()


def create_window():
    global game_overlay
    game_overlay = GameOverlay()
