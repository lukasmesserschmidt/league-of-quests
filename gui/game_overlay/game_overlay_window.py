from PySide6.QtCore import Qt, QTimer

from .map_cover import MapCover
from .ability_cover import AbilityCover
from .summoner_spell_cover import SummonerSpellCover
from .resource_cover import ResourceCover
from .trinket_cover import TrinketCover
from .teleport_cover import TeleportCover
from .. import app
from ..window_base import WindowBase
from ...lol_data.lol_settings import LolSettings
from ...lol_data.lol_window_data import LolWindowData


class GameOverlay(WindowBase):
    def __init__(self):
        super().__init__()
        width, height = app.get_app().primaryScreen().size().toTuple()
        self.setGeometry(0, 0, width, height)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint
            | Qt.WindowTransparentForInput
            | Qt.FramelessWindowHint
        )

        self.overlay_covers = {
            "ability": AbilityCover(self),
            "summoner_spell": SummonerSpellCover(self),
            "map": MapCover(self),
            "trinket": TrinketCover(self),
            "teleport": TeleportCover(self),
            "resource": ResourceCover(self),
        }

        self.main_loop_timer = QTimer(self)
        self.main_loop_timer.timeout.connect(self.main_loop)
        self.main_loop_timer.start(10)

    def main_loop(self):
        if LolWindowData.lol_is_top and LolSettings.get_lol_setting("window_mode") == 2:
            self.show()
        else:
            self.hide()

    # def enable_cover(self, enable: bool, overlay_type: str, *args: int):
    def enable_cover(self, enable: bool, overlay_types: dict):
        for overlay_type, args in overlay_types.items():
            cover = self.overlay_covers[overlay_type]
            if enable:
                cover.show(*args)
            else:
                cover.hide(*args)


def create_game_overlay():
    global game_overlay
    game_overlay = GameOverlay()


def get_game_overlay():
    return game_overlay
