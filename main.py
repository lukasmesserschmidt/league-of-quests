import win32gui


def get_hwnd():
    window_title = "League of Quests"
    class_name = "Qt663QWindowIcon"
    hwnd = win32gui.FindWindow(class_name, window_title)

    return hwnd


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
    hwnd = get_hwnd()

    if hwnd == 0:
        start()
    else:
        win32gui.SetForegroundWindow(hwnd)


if __name__ == "__main__":
    main()
