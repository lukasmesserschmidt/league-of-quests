import win32gui


def get_hwnd():
    window_title = "League of Quests"
    class_name = "Qt663QWindowIcon"
    hwnd = win32gui.FindWindow(class_name, window_title)

    return hwnd


def start():
    import scripts

    scripts.start()


def main():
    hwnd = get_hwnd()

    if hwnd == 0:
        start()
    else:
        win32gui.SetForegroundWindow(hwnd)


if __name__ == "__main__":
    main()
