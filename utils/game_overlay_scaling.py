from ..gui import app

from ..lol_data.lol_settings import LolSettings


def get_overlay_size(min_size, max_size, scale, max_scale):
    _, screen_y = app.app.primaryScreen().size().toTuple()
    min_size = min_size / 2160 * screen_y
    max_size = max_size / 2160 * screen_y
    size = ((max_size - min_size) / max_scale) * scale + min_size

    return size


def get_overlay_pos(x, y):
    screen_x, screen_y = app.app.primaryScreen().size().toTuple()
    ratio = (3840 / 2160) / (screen_x / screen_y)
    from_center_x = (1920 - x) / 3840 * screen_x * ratio
    from_center_x = (1920 - x) / 2160 * screen_y
    x = (screen_x / 2) - from_center_x
    y = y / 2160 * screen_y

    return x, y


def get_scaled_pos(min_x, max_x, min_y, max_y):
    min_x, min_y = get_overlay_pos(min_x, min_y)
    max_x, max_y = get_overlay_pos(max_x, max_y)
    x_diff = min_x - max_x
    y_diff = min_y - max_y
    x = min_x - x_diff * LolSettings.get_global_scale()
    y = min_y - y_diff * LolSettings.get_global_scale()

    return x, y


def get_map_size():
    return get_overlay_size(400, 800, LolSettings.get_map_scale(), 3)


def get_global_size(min_size, max_size):
    return get_overlay_size(min_size, max_size, LolSettings.get_global_scale(), 1)
