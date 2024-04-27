import win32gui
from PySide6.QtCore import QTimer


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
