from PySide6.QtCore import Qt, QTimer

from .map_cover import MapCover
from .ability_cover import AbilityCover
from .summoner_spell_cover import SummonerSpellCover
from .resource_cover import ResourceCover
from .trinket_cover import TrinketCover
from .recall_cover import RecallCover
from ..window_base import WindowBase
from ...lol_data.lol_settings import LolSettings
from ...lol_data.lol_window_data import LolWindowData
from ...utils import user_data
from ...utils.is_game_active import is_game_active
from ...utils.is_program_active import is_program_active
from ...utils.constants import Constants


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
            Constants.ABILITY: {
                "active": set(),
                "reset": {0, 1, 2, 3},
                "cover": AbilityCover(self),
            },
            Constants.SUMMONER_SPELL: {
                "active": set(),
                "reset": {0, 1},
                "cover": SummonerSpellCover(self),
            },
            Constants.RESOURCE: {
                "active": set(),
                "reset": {0, 1},
                "percent": [(0, 0), (1, 0)],
                "cover": ResourceCover(self),
            },
            Constants.TRINKET: {
                "active": set(),
                "reset": {0},
                "cover": TrinketCover(self),
            },
            Constants.RECALL: {
                "active": set(),
                "reset": {0},
                "cover": RecallCover(self),
            },
            Constants.MAP: {"active": set(), "reset": {0}, "cover": MapCover(self)},
        }

        self.main_loop_timer = QTimer(self)
        self.main_loop_timer.timeout.connect(self.main_loop)

        self.hide()

    def start(self):
        self.main_loop_timer.start(100)

    def stop(self):
        self.main_loop_timer.stop()
        for overlay_cover in self.overlay_covers.values():
            overlay_cover["active"].clear()
        self.hide()

    def main_loop(self):
        if (
            is_program_active()
            and is_game_active()
            and LolWindowData.lol_is_top
            and LolSettings.get_lol_setting(Constants.WINDOW_MODE) == 2
        ):
            self.update_covers()
            self.show()
        else:
            self.hide()

    def enable_overlays(
        self,
        overlay_types: dict[Constants, list[int | tuple[int, float | int]]],
        enable: bool,
        owner: object,
    ):
        for overlay_type, args in overlay_types.items():
            if overlay_type == Constants.RESOURCE:
                overlays = set()
                for arg in args:
                    self.overlay_covers[overlay_type]["percent"][arg[0]] = arg
                    overlays.add((arg[0], owner))
            else:
                overlays = {(arg, owner) for arg in args}

            if enable:
                self.overlay_covers[overlay_type]["active"].update(overlays)
            else:
                self.overlay_covers[overlay_type]["active"].difference_update(overlays)

    def update_covers(self):
        for overlay_type, overlay_cover in self.overlay_covers.items():
            cover = overlay_cover["cover"]
            active_overlays = self.get_active_overlays(overlay_type)
            reset_overlays = overlay_cover["reset"].copy()
            reset_overlays.difference_update(active_overlays)

            if overlay_type == Constants.RESOURCE:
                cover.set_percent(*overlay_cover["percent"])

            if reset_overlays:
                cover.hide(*reset_overlays)
            if active_overlays:
                cover.show(*active_overlays)

    def get_active_overlays(self, overlay_type: Constants):
        active_overlays = {
            overlay[0] for overlay in self.overlay_covers[overlay_type]["active"]
        }

        return active_overlays


def create_game_overlay():
    global game_overlay
    game_overlay = GameOverlayWindow()


def get_game_overlay():
    return game_overlay
