import keyboard

from lol_quest.gui import app
from lol_quest.gui import main_menu
from lol_quest.gui import stop_window
from lol_quest.gui import quest_display
from lol_quest.gui.game_overlay import game_overlay_window


def main():
    quest_display.create_quest_display()
    game_overlay_window.create_game_overlay()
    stop_window.create_stop_window()
    main_menu.create_main_menu()

    app.start()
    keyboard.unhook_all()


if __name__ == "__main__":
    main()
