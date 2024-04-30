from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QCursor
import keyboard

from .window_base import WindowBase
from .quest_display_base import Ui_QuestDisplay
from . import app
from ..manager.settings_manager import Settings
from ..utils.game_overlay_scaling import get_map_size


class QuestDisplay(WindowBase):
    def __init__(self):
        super().__init__()
        self.setgeometry()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint
            | Qt.WindowTransparentForInput
            | Qt.FramelessWindowHint
        )

        self.ui = Ui_QuestDisplay()
        self.ui.setupUi(self)

        self.move_timer = QTimer(self)
        self.move_timer.timeout.connect(self.move_to_mouse)
        self.move_timer.start(10)

        self.show()

    def setgeometry(self):
        x, y = app.get_app().primaryScreen().size().toTuple()
        map_size = get_map_size()
        space = get_map_size() * 0.05
        x -= map_size + 250 + space
        y -= 300

        self.setGeometry(x, y, 250, 300)

    def move_to_mouse(self):
        if keyboard.is_pressed("shift"):
            x = QCursor.pos().toTuple()[0] - self.width() / 2
            y = QCursor.pos().toTuple()[1]
            self.move(x, y)

    def get_timer_text(self):
        return self.ui.next_quest_time_label.text()

    def set_timer_text(self, text):
        self.ui.next_quest_time_label.setText(text)

    def set_quest_count(self, count):
        self.ui.quest_count_label.setText(f"{count}/{Settings.get_quest_limit()}")

    def add_widget(self, widget):
        self.ui.quest_frame_layout.addWidget(widget, 1, Qt.AlignRight | Qt.AlignTop)


def create_quest_display():
    global quest_display
    quest_display = QuestDisplay()


def get_quest_display():
    return quest_display
