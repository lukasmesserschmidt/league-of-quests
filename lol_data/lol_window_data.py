import win32gui
from PySide6.QtCore import QTimer

from .lol_settings import LolSettings
from ..utils.user_data import get_monitor_resolution, get_monitor_dpi_resolution


class LolWindowData:
    lol_title = "League of Legends (TM) Client"
    lol_is_top = False

    @classmethod
    def start(cls):
        cls.lol_is_top = False

        cls.check_lol_is_top_timer = QTimer()
        cls.check_lol_is_top_timer.timeout.connect(cls.check_lol_is_top)
        cls.check_lol_is_top_timer.start(100)

    @classmethod
    def check_lol_is_top(cls):
        top_window = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(top_window)

        cls.lol_is_top = title == cls.lol_title

        return cls.lol_is_top

    @classmethod
    def get_window_mode(cls):
        window_mode = LolSettings.get_lol_setting("window_mode")

        return window_mode

    @classmethod
    def get_resolution(cls):
        width = LolSettings.get_lol_setting("width")
        height = LolSettings.get_lol_setting("height")

        return width, height

    @classmethod
    def get_scaled_resolution(cls):
        lol_resolution = cls.get_resolution()
        monitor_resolution = get_monitor_resolution()
        monitor_dpi_resolution = get_monitor_dpi_resolution()
        scaled_resolution = []

        for lol_res, monitor_res, monitor_dpi_res in zip(
            lol_resolution, monitor_resolution, monitor_dpi_resolution
        ):
            scaled_res = lol_res / monitor_res * monitor_dpi_res
            scaled_resolution.append(scaled_res)

        return scaled_resolution

    @classmethod
    def get_scaled_pos(cls):
        monitor_pos = cls.get_pos()
        monitor_resolution = get_monitor_resolution()
        monitor_dpi_resolution = get_monitor_dpi_resolution()
        scaled_pos = []

        for pos, monitor_res, monitor_dpi_res in zip(
            monitor_pos, monitor_resolution, monitor_dpi_resolution
        ):
            pos = pos / monitor_res * monitor_dpi_res
            scaled_pos.append(pos)

        return scaled_pos

    @classmethod
    def get_geometry(cls):
        hwnd = win32gui.FindWindow(None, cls.lol_title)
        rect = win32gui.GetWindowRect(hwnd)

        return rect

    @classmethod
    def get_pos(cls):
        rect = cls.get_geometry()
        x = rect[0]
        y = rect[1]

        return x, y

    @classmethod
    def get_size(cls):
        rect = cls.get_geometry()
        width = rect[2] - rect[0]
        height = rect[3] - rect[1]

        return width, height
