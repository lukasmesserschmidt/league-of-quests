"""
This module contains functions for scaling the game overlay to the League of Legends settings.
"""

from ..lol_data.lol_settings import LolSettings
from ..lol_data.lol_window_data import LolWindowData
from ..utils.constants import Constants


def get_scaled_overlay_size(min_size, max_size, scale, max_scale):
    """
    Returns the size of the overlay scaled to the League of Legends settings.
    """
    _, scaled_y_resolution = LolWindowData.get_scaled_resolution()
    min_size = min_size / 2160 * scaled_y_resolution
    max_size = max_size / 2160 * scaled_y_resolution
    size = ((max_size - min_size) / max_scale) * scale + min_size

    return size


def get_scaled_pos(min_x, max_x, min_y, max_y, scale, max_scale):
    """
    Returns the position of the overlay scaled to the League of Legends settings.
    """
    min_x, min_y = get_overlay_pos(min_x, min_y)
    max_x, max_y = get_overlay_pos(max_x, max_y)
    x_diff = min_x - max_x
    y_diff = min_y - max_y
    x = min_x - x_diff * scale / max_scale
    y = min_y - y_diff * scale / max_scale

    return x, y


def get_overlay_pos(x, y):
    """
    Returns the position of the overlay scaled to the LolWindowData.
    """
    scaled_x_resolution, scaled_y_resolution = LolWindowData.get_scaled_resolution()
    window_x, window_y = LolWindowData.get_scaled_pos()
    from_center_x = (1920 - x) / 2160 * scaled_y_resolution
    from_bottom_y = (2160 - y) / 2160 * scaled_y_resolution
    x = window_x + (scaled_x_resolution / 2) - from_center_x
    y = window_y + scaled_y_resolution - from_bottom_y

    return x, y


def get_map_size():
    """
    Returns the size of the map scaled to the League of Legends map scale setting.
    """
    return get_scaled_overlay_size(
        400, 800, LolSettings.get_lol_setting(Constants.MAP_SCALE), 3
    )


def get_global_size(min_size, max_size):
    """
    Returns the size of a overlay scaled to the League of Legends global scale setting.
    """
    return get_scaled_overlay_size(
        min_size, max_size, LolSettings.get_lol_setting(Constants.GLOBAL_SCALE), 1
    )


def get_global_pos(min_x, max_x, min_y, max_y):
    """
    Returns the position of a overlay scaled to the League of Legends global scale setting.
    """
    return get_scaled_pos(
        min_x,
        max_x,
        min_y,
        max_y,
        LolSettings.get_lol_setting(Constants.GLOBAL_SCALE),
        1,
    )
