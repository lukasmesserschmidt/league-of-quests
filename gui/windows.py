from .main_menu import MainWindow
from .quest_display import QuestDisplay
from .game_overlay.game_overlay_window import GameOverlay


def create_windows():
    global main_menu
    global quest_display
    global game_overlay

    main_menu = MainWindow()
    quest_display = QuestDisplay()
    game_overlay = GameOverlay()

    main_menu.show()
    quest_display.show()
    game_overlay.show()
