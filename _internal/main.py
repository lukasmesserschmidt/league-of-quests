import ctypes


def is_window_open():
    hwnd = get_hwnd()

    return hwnd != 0


def get_hwnd():
    window_title = "League of Quests"
    class_name = "Qt663QWindowIcon"

    return ctypes.windll.user32.FindWindowW(class_name, window_title)


def start():
    import keyboard

    from lol_quest.gui import app
    from lol_quest.gui import main_menu
    from lol_quest.gui import stop_window
    from lol_quest.gui import quest_display
    from lol_quest.gui.game_overlay import game_overlay_window

    quest_display.create_quest_display()
    game_overlay_window.create_game_overlay()
    stop_window.create_stop_window()
    main_menu.create_main_menu()

    app.start()
    keyboard.unhook_all()


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
