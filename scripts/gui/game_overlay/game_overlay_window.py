"""
This module contains the GameOverlayWindow class, which displays the game overlay.
"""

from contextlib import suppress
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
    """
    A class for displaying the game overlay.
    """

    def __init__(self):
        super().__init__()

        # set window attributes
        width, height = user_data.get_monitor_dpi_resolution()
        self.setGeometry(0, 0, width, height)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint
            | Qt.WindowTransparentForInput
            | Qt.FramelessWindowHint
        )

        # init overlay covers dict
        self.overlay_covers_dict = {
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
                "percent": [[0, 0], [1, 0]],
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

        # update loop
        self._update_loop_timer = QTimer(self)
        self._update_loop_timer.timeout.connect(self._update_loop)

        self.hide()

    # control
    def start(self):
        """
        Starts the game overlay window update loop.
        """
        self._update_loop_timer.start(100)

    def stop(self):
        """
        Stops the game overlay window update loop and clears active overlays.
        """
        self._update_loop_timer.stop()
        for overlay_cover in self.overlay_covers_dict.values():
            overlay_cover["active"].clear()
        self.hide()

    # update loop
    def _update_loop(self):
        if (
            is_program_active()
            and is_game_active()
            and LolWindowData.lol_is_top
            and LolSettings.get_lol_setting(Constants.WINDOW_MODE) == 2
        ):
            self._update_covers()
            self.show()
        else:
            self.hide()

    def _update_covers(self):
        for overlay_type, overlay_cover in self.overlay_covers_dict.items():
            cover = overlay_cover["cover"]

            active_overlays = {overlay[0] for overlay in overlay_cover["active"]}

            reset_overlays = overlay_cover["reset"].copy()
            reset_overlays.difference_update(active_overlays)

            if overlay_type == Constants.RESOURCE:
                cover.set_percent(*overlay_cover["percent"])

            with suppress(Exception):
                if reset_overlays:
                    cover.hide(*reset_overlays)
                if active_overlays:
                    cover.show(*active_overlays)

    # overlays control
    def enable_overlays(
        self,
        overlay_types: dict[Constants, list[int | tuple[int, float | int]]],
        enable: bool,
        owner: object,
    ):
        """
        Enable or disable overlays based on the given overlay types and owner.

        Args:
            overlay_types (dict[Constants, list[int | tuple[int, float | int]]]): A dictionary mapping overlay types to a list of arguments.
            enable (bool): A boolean indicating whether to enable or disable the overlays.
            owner (object): The owner of the overlays.
        """
        for overlay_type, args in overlay_types.items():
            if overlay_type == Constants.RESOURCE:
                overlays = set()
                for arg in args:
                    self.overlay_covers_dict[overlay_type]["percent"][arg[0]][1] = arg[
                        1
                    ]
                    overlays.add((arg[0], owner))
            else:
                overlays = {(arg, owner) for arg in args}

            if enable:
                self.overlay_covers_dict[overlay_type]["active"].update(overlays)
            else:
                self.overlay_covers_dict[overlay_type]["active"].difference_update(
                    overlays
                )
