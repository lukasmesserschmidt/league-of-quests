import keyboard

from .gui import app
from .gui import main_menu
from .gui import quest_display
from .gui.game_overlay import game_overlay_window


quest_display.create_quest_display()
game_overlay_window.create_game_overlay()
main_menu.create_main_menu()

app.start()
keyboard.unhook_all()
