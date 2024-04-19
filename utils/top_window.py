import win32gui


def get_top_window_is_lol():
    top_window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(top_window)

    if title == lol_title:
        return True

    return False


lol_title = "League of Legends (TM) Client"
