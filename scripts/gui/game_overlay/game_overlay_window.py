from PySide6.QtCore import Qt, QTimer

from .map_cover import MapCover
from .ability_cover import AbilityCover
from .summoner_spell_cover import SummonerSpellCover
from .resource_cover import ResourceCover
from .trinket_cover import TrinketCover
from .teleport_cover import TeleportCover
from ..window_base import WindowBase
from ...lol_data.lol_settings import LolSettings
from ...lol_data.lol_window_data import LolWindowData
from ...utils import user_data
from ...utils.is_game_active import is_game_active
from ...utils.is_program_active import is_program_active


class GameOverlayWindow(WindowBase):
    def __init__(self):
        super().__init__()
        width, height = user_data.get_monitor_dpi_resolution()
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

        self.hide()

    def start(self):
        self.main_loop_timer.start(100)

    def stop(self):
        self.main_loop_timer.stop()
        self.hide()

    def main_loop(self):
        if (
            is_program_active()
            and is_game_active()
            and LolWindowData.lol_is_top
            and LolSettings.get_lol_setting("window_mode") == 2
        ):
            self.show()
        else:
            self.hide()

    def enable_cover(self, enable: bool, overlay_types: dict[str, list[int]]):
        if LolWindowData.lol_is_top and is_game_active():
            for overlay_type, args in overlay_types.items():
                cover = self.overlay_covers[overlay_type]
                if enable:
                    cover.show(*args)
                else:
                    cover.hide(*args)


def create_game_overlay():
    global game_overlay
    game_overlay = GameOverlayWindow()


def get_game_overlay():
    return game_overlay
