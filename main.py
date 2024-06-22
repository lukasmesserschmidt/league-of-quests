"""
This module starts the program if its not already running.
"""

import win32gui


def get_hwnd():
    """
    Gets the hwnd of the League of Quests window.
    """
    window_title = "League of Quests"
    class_name = "Qt663QWindowIcon"
    hwnd = win32gui.FindWindow(class_name, window_title)

    return hwnd


def start():
    """
    Starts the program.
    """
    import scripts

    scripts.start()


def main():
    """
    Starts the program if its not already running.
    """
    hwnd = get_hwnd()

    if hwnd == 0:
        start()
    else:
        win32gui.SetForegroundWindow(hwnd)


if __name__ == "__main__":
    main()
