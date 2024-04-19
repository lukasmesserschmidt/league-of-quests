from PySide6.QtCore import Qt
import keyboard

from .gui import app
from .gui import main_menu
from .gui import quest_display
from .gui.game_overlay import game_overlay_window

from .gui.quest_display_frame import QuestDisplayFrame


# app.create_app()
# main_menu.create_window()
# quest_display.create_window()
# game_overlay_window.create_window()

for _ in range(0):
    f = QuestDisplayFrame()
    quest_display.quest_display.add_widget(f)

app.start()
keyboard.unhook_all()
