from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QCursor
from pynput import mouse

from .window_base import WindowBase
from .quest_display_base import Ui_QuestDisplay
from . import app
from ..manager.settings_manager import Settings
from ..lol_data.lol_settings import LolSettings
from ..lol_data.lol_window_data import LolWindowData
from ..utils.game_overlay_scaling import get_map_size
from ..utils.is_lol_installed import is_lol_installed


class QuestDisplay(WindowBase):
    def __init__(self):
        super().__init__()

        if is_lol_installed():
            self.setgeometry()
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setWindowFlags(
                Qt.WindowStaysOnTopHint
                | Qt.WindowTransparentForInput
                | Qt.FramelessWindowHint
            )

            self.ui = Ui_QuestDisplay()
            self.ui.setupUi(self)

            self.start_x_diff = 0
            self.start_y_diff = 0
            self.last_width = self.geometry().width()
            self.dragg = False

            self.mouse_listener = mouse.Listener(on_click=self.on_click)
            self.mouse_listener.start()

            self.main_loop_timer = QTimer(self)
            self.main_loop_timer.timeout.connect(self.main_loop)
            self.main_loop_timer.start(10)

            self.show()

    def setgeometry(self):
        x, y = app.get_app().primaryScreen().size().toTuple()
        map_size = get_map_size()
        space = get_map_size() * 0.05
        x -= (
            (map_size + space) if not LolSettings.get_lol_setting("flip_map") else 0
        ) + 250
        y -= 300

        self.setGeometry(x, y, 250, 300)

    def main_loop(self):
        self.move_to_mouse()
        self.stretch_to_left()

        if LolWindowData.lol_is_top:
            self.show()
        else:
            self.hide()

    def on_click(self, x, y, button, pressed):
        mouse_x, mouse_y = QCursor.pos().toTuple()
        left_x, top_y = self.geometry().topLeft().toTuple()
        right_x, bottom_y = self.geometry().bottomRight().toTuple()
        if (
            pressed
            and button == mouse.Button.left
            and left_x < mouse_x < right_x
            and top_y < mouse_y < bottom_y
        ):

            self.start_x_diff = mouse_x - left_x
            self.start_y_diff = mouse_y - top_y

            self.dragg = True
        else:
            self.dragg = False

    def move_to_mouse(self):
        if self.dragg:
            mouse_x, mouse_y = QCursor.pos().toTuple()
            x = mouse_x - self.start_x_diff
            y = mouse_y - self.start_y_diff
            self.move(x, y)

    def stretch_to_left(self):
        current_width = self.geometry().width()
        if current_width != self.last_width:
            width_diff = current_width - self.last_width
            x = self.geometry().left() - width_diff
            y = self.geometry().top()

            self.move(x, y)
            self.last_width = current_width

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
