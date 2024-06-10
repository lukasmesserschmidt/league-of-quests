from ..gui.game_overlay.game_overlay_window import get_game_overlay
from ..utils.constants import Constants


class EnableOverlayBase:
    overlay_types: dict[Constants, list[int | tuple[int, float | int]]]

    @classmethod
    def set_overlay_type(cls, *args: tuple[Constants, list[tuple[int, float | int]]]):
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
        if overlay_types is None:
            overlay_types = cls.overlay_types

        get_game_overlay().enable_overlays(overlay_types, enable, cls)
