"""
This module contains the Base class for all quests and restrictions that use overlays.	
"""

from ..gui.game_overlay.game_overlay_window import GameOverlayWindow
from ..utils.constants import Constants


class EnableOverlayBase:
    """
    This class is the base class for all enable overlays.
    """

    # deffine overlay types
    overlay_types: dict[Constants, list[int | tuple[int, float | int]]]

    @classmethod
    def set_overlay_type(cls, *args: tuple[Constants, list[tuple[int, float | int]]]):
        """
        Sets the overlay types.
        """
        for overlay_types in args:
            overlay_type = overlay_types[0]
            overlay_nums = overlay_types[1]

            cls.overlay_types[overlay_type] = overlay_nums

    @classmethod
    def enable_overlays(
        cls,
        enable: bool,
        overlay_types: dict[Constants, list[int | tuple[int, float | int]]] = None,
    ):
        """
        Enables or disables the overlays deffined in overlay_types.
        """
        if overlay_types is None:
            overlay_types = cls.overlay_types

        GameOverlayWindow.get_instance().enable_overlays(overlay_types, enable, cls)
