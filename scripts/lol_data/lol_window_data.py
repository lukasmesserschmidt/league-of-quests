import win32gui
from PySide6.QtCore import QTimer

from .lol_settings import LolSettings
from ..utils import user_data


class LolWindowData:
    lol_title = "League of Legends (TM) Client"
    lol_is_top = False
    check_lol_is_top_timer = None

    @classmethod
    def start(cls):
        if cls.check_lol_is_top_timer is None:
            cls.check_lol_is_top_timer = QTimer()
            cls.check_lol_is_top_timer.timeout.connect(cls._check_lol_is_top)

        cls.lol_is_top = False
        cls.check_lol_is_top_timer.start(100)

    @classmethod
    def stop(cls):
        if cls.check_lol_is_top_timer is not None:
            cls.check_lol_is_top_timer.stop()
            cls.lol_is_top = False

    @classmethod
    def _check_lol_is_top(cls):
        top_window = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(top_window)

        cls.lol_is_top = title == cls.lol_title

    @classmethod
    def get_lol_hwnd(cls):
        class_name = "RiotWindowClass"
        hwnd = win32gui.FindWindow(class_name, cls.lol_title)

        return hwnd

    @classmethod
    def is_lol_open(cls):
        hwnd = cls.get_lol_hwnd()

        return hwnd != 0

    @classmethod
    def get_window_mode(cls):
        window_mode = LolSettings.get_lol_setting("window_mode")

        return window_mode

    @classmethod
    def _get_geometry(cls):
        hwnd = win32gui.FindWindow(None, cls.lol_title)
        rect = win32gui.GetWindowRect(hwnd)

        return rect

    @classmethod
    def _get_resolution(cls):
        width = LolSettings.get_lol_setting("width")
        height = LolSettings.get_lol_setting("height")

        return width, height

    @classmethod
    def _get_pos(cls):
        rect = cls._get_geometry()
        x = rect[0]
        y = rect[1]

        return x, y

    @classmethod
    def _get_scaled_values(cls, values: list):
        monitor_resolution = user_data.get_monitor_resolution()
        monitor_dpi_resolution = user_data.get_monitor_dpi_resolution()
        scaled_values = []

        for value, monitor_res, monitor_dpi_res in zip(
            values, monitor_resolution, monitor_dpi_resolution
        ):
            result = value / monitor_res * monitor_dpi_res
            scaled_values.append(result)

        return scaled_values

    @classmethod
    def get_scaled_resolution(cls):
        lol_resolution = cls._get_resolution()
        scaled_resolution = cls._get_scaled_values(lol_resolution)

        return scaled_resolution

    @classmethod
    def get_scaled_pos(cls):
        monitor_position = cls._get_pos()
        scaled_pos = cls._get_scaled_values(monitor_position)

        return scaled_pos
