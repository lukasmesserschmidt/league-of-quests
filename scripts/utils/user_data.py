"""
This module contains functions for getting user data.
"""

import win32api

from ..gui.app import get_app


def get_monitor_resolution():
    """
    Returns the resolution of the users monitor.
    """
    width = win32api.GetSystemMetrics(0)
    height = win32api.GetSystemMetrics(1)

    return (width, height)


def get_monitor_dpi_resolution():
    """
    Returns the dpi resolution of the users monitor.
    """
    return get_app().primaryScreen().size().toTuple()
