import win32api

from ..gui.app import get_app


def get_monitor_resolution():
    width = win32api.GetSystemMetrics(0)
    height = win32api.GetSystemMetrics(1)

    return (width, height)


def get_monitor_dpi_resolution():
    return get_app().primaryScreen().size().toTuple()
