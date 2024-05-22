from ..lol_data.lol_settings import LolSettings
from ..lol_data.lol_window_data import LolWindowData


def get_scaled_overlay_size(min_size, max_size, scale, max_scale):
    _, scaled_y_resolution = LolWindowData.get_scaled_resolution()
    min_size = min_size / 2160 * scaled_y_resolution
    max_size = max_size / 2160 * scaled_y_resolution
    size = ((max_size - min_size) / max_scale) * scale + min_size

    return size


def get_scaled_pos(min_x, max_x, min_y, max_y, scale, max_scale):
    min_x, min_y = get_overlay_pos(min_x, min_y)
    max_x, max_y = get_overlay_pos(max_x, max_y)
    x_diff = min_x - max_x
    y_diff = min_y - max_y
    x = min_x - x_diff * scale / max_scale
    y = min_y - y_diff * scale / max_scale

    return x, y


def get_overlay_pos(x, y):
    scaled_x_resolution, scaled_y_resolution = LolWindowData.get_scaled_resolution()
    window_x, window_y = LolWindowData.get_scaled_pos()
    from_center_x = (1920 - x) / 2160 * scaled_y_resolution
    from_bottom_y = (2160 - y) / 2160 * scaled_y_resolution
    x = window_x + (scaled_x_resolution / 2) - from_center_x
    y = window_y + scaled_y_resolution - from_bottom_y

    return x, y


def get_map_size():
    return get_scaled_overlay_size(
        400, 800, LolSettings.get_lol_setting("map_scale"), 3
    )


def get_global_size(min_size, max_size):
    return get_scaled_overlay_size(
        min_size, max_size, LolSettings.get_lol_setting("global_scale"), 1
    )


def get_global_pos(min_x, max_x, min_y, max_y):
    return get_scaled_pos(
        min_x, max_x, min_y, max_y, LolSettings.get_lol_setting("global_scale"), 1
    )
