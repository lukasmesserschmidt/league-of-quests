from PySide6.QtCore import QTimer
from PySide6.QtCore import Signal

from .window_base import WindowBase
from .stop_window_base import Ui_StopWindow
from ..utils.is_game_active import is_game_active


class StopWindow(WindowBase):
    stoped = Signal()

    def __init__(self):
        super().__init__()

        self.ui = Ui_StopWindow()
        self.ui.setupUi(self)

        self.config_widgets()

        self.hide()

    def config_widgets(self):
        self.ui.stop_button.clicked.connect(self.stop_command)

    def stop_command(self):
        self.stop()
        self.stoped.emit()

    def start(self):
        self.show()
        self.game_running = True
        self.main_loop_timer = QTimer(self)
        self.main_loop_timer.timeout.connect(self.main_loop)
        self.main_loop_timer.start(100)

    def stop(self):
        self.hide()
        self.main_loop_timer.deleteLater()

    def main_loop(self):
        if not is_game_active() and self.game_running:
            self.stop_command()
            self.game_running = False


def create_stop_window():
    global stop_window
    stop_window = StopWindow()


def get_stop_window():
    return stop_window
