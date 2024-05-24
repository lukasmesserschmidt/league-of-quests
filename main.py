import ctypes


def is_window_open():
    hwnd = get_hwnd()

    return hwnd != 0


def get_hwnd():
    window_title = "League of Quests"
    class_name = "Qt663QWindowIcon"

    return ctypes.windll.user32.FindWindowW(class_name, window_title)


def start():
    from scripts.gui import app
    from scripts.gui import main_menu
    from scripts.gui import stop_window
    from scripts.gui import quest_display
    from scripts.gui.game_overlay import game_overlay_window

    game_overlay_window.create_game_overlay()
    quest_display.create_quest_display()
    stop_window.create_stop_window()
    main_menu.create_main_menu()

    app.start()


def main():
    global user32
    user32 = ctypes.windll.user32

    if not is_window_open():
        start()
    else:
        hwnd = get_hwnd()
        user32.SetForegroundWindow(hwnd)


if __name__ == "__main__":
    main()
