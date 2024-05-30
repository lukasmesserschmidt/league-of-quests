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

        # self.overlay_covers = {
        #     Constants.ABILITY: AbilityCover(self),
        #     Constants.SUMMONER_SPELL: SummonerSpellCover(self),
        #     Constants.TRINKET: TrinketCover(self),
        #     Constants.TELEPORT: TeleportCover(self),
        #     Constants.RESOURCE: ResourceCover(self),
        #     Constants.MAP: MapCover(self),
        # }

        self.overlay_covers = {
            Constants.ABILITY: {
                "nums": [False, False, False, False],
                "cover": AbilityCover(self),
            },
            Constants.SUMMONER_SPELL: {
                "nums": [False, False],
                "cover": SummonerSpellCover(self),
            },
            Constants.RESOURCE: {
                "nums": [(False, 0), (False, 0)],
                "cover": ResourceCover(self),
            },
            Constants.TRINKET: {"nums": [False], "cover": TrinketCover(self)},
            Constants.TELEPORT: {"nums": [False], "cover": TeleportCover(self)},
            Constants.MAP: {"nums": [False], "cover": MapCover(self)},
        }

        self.main_loop_timer = QTimer(self)
        self.main_loop_timer.timeout.connect(self.main_loop)

        self.hide()

    def start(self):
        self.main_loop_timer.start(500)

    def stop(self):
        self.main_loop_timer.stop()
        self.hide()

    def main_loop(self):
        if (
            is_program_active()
            and is_game_active()
            and LolWindowData.lol_is_top
            and LolSettings.get_lol_setting(Constants.WINDOW_MODE) == 2
        ):
            self.show()
            self.update_covers()
        else:
            self.hide()

    # def enable_cover(self, enable: bool, overlay_types: dict[Enum, list[int]]):
    #     for overlay_type, args in overlay_types.items():
    #         cover = self.overlay_covers[overlay_type]
    #         if enable:
    #             if LolWindowData.lol_is_top and is_game_active():
    #                 cover.show(*args)
    #         else:
    #             cover.hide(*args)

    def enable_cover(self, enable: bool, overlay_types: dict[Constants, list[int]]):
        for overlay_type, args in overlay_types.items():
            for arg in args:
                if overlay_type != Constants.RESOURCE:
                    self.overlay_covers[overlay_type]["nums"][arg] = enable
                else:
                    percent = arg[1]
                    arg = arg[0]
                    self.overlay_covers[overlay_type]["nums"][arg] = (enable, percent)

    def update_covers(self):
        for overlay_cover in self.overlay_covers.values():
            cover = overlay_cover["cover"]
            overlay_nums = overlay_cover["nums"]
            cover.update_cover(*overlay_nums)


def create_game_overlay():
    global game_overlay
    game_overlay = GameOverlayWindow()


def get_game_overlay():
    return game_overlay
