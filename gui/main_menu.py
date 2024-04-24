from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QCloseEvent
from PySide6.QtGui import QIcon
import threading

from .main_menu_base import Ui_MainWindow
from ..manager.main_manager import MainManager
from ..manager.settings_manager import Settings
from ..lol_data.get_lol_settings import GetLolSettings
from ..lol_data.live_client_data import LiveClientData
from ..lol_data.game_data import GameData
from ..manager.active_quest_frames import active_quest_frames


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # config
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("lol_quest/graphics/loq_icon.ico"))

        self.config_widgets()

        # import settings
        Settings.import_settings()

        self.show()

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

    def set_start_button(self, text: str, color: tuple, command):
        self.ui.start_button.setText(text)
        self.ui.start_button.setStyleSheet(
            "QPushButton{\n"
            "color: rgb(235, 235, 235);\n"
            f"background-color: rgb{color};\n"
            "border-radius: 5px\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color: rgb(20, 72, 112);\n"
            "}"
        )
        self.ui.start_button.clicked.disconnect()
        self.ui.start_button.clicked.connect(command)

    def start_command(self):
        self.set_start_button("Waiting", ((52, 54, 56)), self.stop_command)
        self.start = False
        self.start_timer = QTimer(self)
        self.start_timer.timeout.connect(self.wait_for_start)
        self.start_timer.start(100)

        self.terminate_flag = False
        self.wait_for_game_start_thread = threading.Thread(
            target=self.wait_for_game_start
        )
        self.wait_for_game_start_thread.start()

    def stop_command(self):
        self.set_start_button("Start", (31, 106, 165), self.start_command)
        self.start_timer.deleteLater()

    def wait_for_start(self):
        if self.start:
            self.stop_command()
            Settings.update(self.ui)
            MainManager.start()
            # self.hide()

    def wait_for_game_start(self):
        while self.ui.start_button.text() == "Waiting":
            if LiveClientData.all_data and GameData.get_game_time() > 0:
                self.start = True
                break

            if self.terminate_flag:
                break

    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        try:
            self.terminate_flag = True
            self.wait_for_game_start_thread.join()
        except:
            pass

        try:
            MainManager.stop()
        except:
            pass

        GetLolSettings.stop()

        QApplication.quit()


main_menu = MainWindow()


def create_window():
    global main_menu
    main_menu = MainWindow()
