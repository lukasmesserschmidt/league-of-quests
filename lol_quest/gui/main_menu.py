from contextlib import suppress
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QCloseEvent

from .main_menu_base import Ui_MainWindow
from .quest_display import get_quest_display
from .game_overlay.game_overlay_window import get_game_overlay
from .stop_window import get_stop_window
from ..manager.main_manager import MainManager
from ..manager.settings_manager import Settings
from ..lol_data.get_lol_settings import GetLolSettings
from ..lol_data.lol_window_data import LolWindowData
from ..lol_data.get_live_client_data import GetLiveClientData
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.is_lol_installed import is_lol_installed
from ..utils.is_game_active import is_game_active


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.config_widgets()

        self.start()

        self.show()

    # config
    def config_widgets(self):
        self.ui.quest_on_death_checkbox.stateChanged.connect(
            lambda state: self.check_checkbox(self.ui.quest_after_time_checkbox, state)
        )

        self.ui.quest_after_time_checkbox.stateChanged.connect(
            lambda state: self.check_checkbox(self.ui.quest_on_death_checkbox, state)
        )

        self.ui.start_button.clicked.connect(self.start_command)

        get_stop_window().closed.connect(self.close)
        get_stop_window().stoped.connect(self.stop)

        get_quest_display().closed.connect(self.close)

        get_game_overlay().closed.connect(self.close)

    def check_checkbox(self, checkbox, state):
        if state == 0:
            checkbox.setChecked(True)

    def start(self):
        self.game_start = False
        self.main_loop_timer = QTimer(self)
        self.main_loop_timer.timeout.connect(self.main_loop)
        self.main_loop_timer.start(100)

    def stop(self):
        MainManager.stop()
        self.show()
        self.start()

    # main
    def main_loop(self):
        if not is_lol_installed():
            self.set_start_button("N/A", (52, 54, 56))
            self.ui.info_label.setText("League of Legends is not installed!")
            self.ui.info_label.show()
        elif LolWindowData.get_window_mode() != 2:
            self.set_start_button("N/A", (52, 54, 56))
            self.ui.info_label.setText("LoL must be in borderless window mode!")
            self.ui.info_label.show()
        elif self.ui.start_button.text() == "N/A":
            self.set_start_button("Start", (31, 106, 165), self.start_command)

        if self.game_start:
            if ActivePlayerData.get_champion_name() != "Aphelios":
                self.hide()
                self.stop_command()
                self.main_loop_timer.deleteLater()
                Settings.update(self.ui)
                MainManager.start()
                get_stop_window().start()
            else:
                self.stop_command()
                self.set_start_button("Start", (31, 106, 165), self.start_command)
                self.ui.info_label.setText("Not playable with Aphelios!")
                self.ui.info_label.show()

    def start_command(self):
        self.set_start_button("Waiting", (52, 54, 56), self.stop_command)
        self.game_start = False

        self.wait_for_game_start_timer = QTimer(self)
        self.wait_for_game_start_timer.timeout.connect(self.wait_for_game_start)
        self.wait_for_game_start_timer.start(100)

    def wait_for_game_start(self):
        if is_game_active():
            self.game_start = True

    def stop_command(self):
        self.wait_for_game_start_timer.deleteLater()
        self.set_start_button("Start", (31, 106, 165), self.start_command)
        self.game_start = False

    # events
    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        get_game_overlay().close()
        get_quest_display().close()
        self.hide()

        with suppress(Exception):
            self.main_loop_timer.deleteLater()
        with suppress(Exception):
            self.wait_for_game_start_timer.deleteLater()

        MainManager.stop()

        with suppress(Exception):
            LolWindowData.stop()
        with suppress(Exception):
            GetLiveClientData.stop()
        with suppress(Exception):
            GetLolSettings.stop()

        QApplication.quit()

    # utils
    def set_start_button(self, text: str, color: tuple, command=None):
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
        with suppress(Exception):
            self.ui.start_button.clicked.disconnect()
        if command:
            self.ui.start_button.clicked.connect(command)

        self.ui.info_label.hide()


def create_main_menu():
    global main_menu
    main_menu = MainMenu()


def get_main_menu():
    return main_menu
