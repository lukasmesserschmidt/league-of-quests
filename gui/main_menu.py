from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QCloseEvent
from PySide6.QtGui import QIcon

from .main_menu_base import Ui_MainWindow
from ..settings_manager import Settings
from ..lol_data.live_game_data import LolData


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # config
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("lol_quest/graphics/loq_icon.ico"))

        self.config_widgets()

        # import settings
        Settings.import_settings()

    def config_widgets(self):
        self.config_checkbox()
        self.config_button()

    def config_checkbox(self):
        self.ui.quest_on_death_checkbox.stateChanged.connect(
            lambda state: self.check_checkbox(self.ui.quest_after_time_checkbox, state)
        )

        self.ui.quest_after_time_checkbox.stateChanged.connect(
            lambda state: self.check_checkbox(self.ui.quest_on_death_checkbox, state)
        )

    def check_checkbox(self, checkbox, state):
        if state == 0:
            checkbox.setChecked(True)

    def config_button(self):
        self.ui.start_button.clicked.connect(self.start_command)

    def start_command(self):
        Settings.update(self.ui)
        pass

    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        QApplication.quit()
