import win32gui
from PySide6.QtCore import QTimer


def start():
    global lol_is_top
    lol_is_top = False

    timer = QTimer()
    timer.timeout.connect(check_top_window_is_lol)
    timer.start(1)


def check_top_window_is_lol():
    global lol_is_top

    top_window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(top_window)

    if title == lol_title:
        lol_is_top = True

    lol_is_top = False


lol_title = "League of Legends (TM) Client"
