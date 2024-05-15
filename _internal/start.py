import ctypes

import run


def is_window_open():
    hwnd = get_hwnd()

    return hwnd != 0


def get_hwnd():
    window_title = "League of Quests"
    class_name = "Qt663QWindowIcon"

    return ctypes.windll.user32.FindWindowW(class_name, window_title)


def main():
    global user32
    user32 = ctypes.windll.user32

    if not is_window_open():
        run.main()
    else:
        hwnd = get_hwnd()
        user32.SetForegroundWindow(hwnd)


if __name__ == "__main__":
    main()
