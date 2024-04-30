from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal

from .window_base import WindowBase
from .stop_window_base import Ui_StopWindow


class StopWindow(WindowBase):
    stop = Signal()

    def __init__(self):
        super().__init__()

        self.ui = Ui_StopWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("lol_quest/graphics/loq_icon.ico"))

        self.config_widgets()

        self.hide()

    def config_widgets(self):
        self.ui.stop_button.clicked.connect(self.stop_command)

    def stop_command(self):
        self.hide()
        self.stop.emit()


def create_stop_window():
    global stop_window
    stop_window = StopWindow()


def get_stop_window():
    return stop_window
