import os
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QCloseEvent

from .main_menu_base import Ui_MainWindow
from .quest_display import get_quest_display
from .game_overlay.game_overlay_window import get_game_overlay
from .stop_window import get_stop_window
from ..manager.main_manager import MainManager
from ..manager.settings_manager import SettingsManager
from ..lol_data.lol_window_data import LolWindowData
from ..lol_data.get_lol_settings import GetLolSettings
from ..lol_data.active_player_data import ActivePlayerData
from ..lol_data.game_data import GameData
from ..lol_data.get_lol_paths import get_lol_settings_path, get_game_cfg_path
from ..utils.is_game_active import is_game_active
from ..utils.is_lol_installed import is_lol_installed


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stop_window = get_stop_window()
        self.quest_display = get_quest_display()
        self.game_overlay = get_game_overlay()

        self.config_widgets()

        self.main_loop_timer = QTimer(self)
        self.main_loop_timer.timeout.connect(self.main_loop)

        if is_lol_installed():
            self.start()
        else:
            self.set_start_button("N/A", (52, 54, 56))
            self.ui.info_label.setText(
                "League of Legends is not installed\n(install League of Legends and restart)!"
            )
            self.ui.info_label.show()

        self.show()

    # config
    def config_widgets(self):
        # checkboxes
        self.ui.quest_on_death_checkbox.stateChanged.connect(
            lambda state: self.set_checkbox(self.ui.quest_after_time_checkbox, state)
        )

        self.ui.quest_after_time_checkbox.stateChanged.connect(
            lambda state: self.set_checkbox(self.ui.quest_on_death_checkbox, state)
        )

        # start button
        self.ui.start_button.clicked.connect(self.start_button_command)

        # connections
        self.stop_window.closed.connect(self.close)
        self.stop_window.stoped.connect(self.stop_game)

        self.quest_display.closed.connect(self.close)

        self.game_overlay.closed.connect(self.close)

    def set_checkbox(self, checkbox, state):
        if state == False:
            checkbox.setChecked(True)

    def start_button_command(self):
        self.start_state = (
            "started" if self.start_state == "not_started" else "not_started"
        )

    def start(self):
        self.start_state = "not_started"
        self.set_start_button("Start", (31, 106, 165), True)
        self.main_loop_timer.start(100)
        self.show()

    def stop_game(self):
        MainManager.stop_game()
        self.start()

    # main
    def main_loop(self):
        self.update_start_button()
        self.check_lol_settings()
        self.check_game_status()

    def update_start_button(self):
        if self.start_state == "started":
            self.set_start_button("Waiting", (52, 54, 56), True)
        elif self.start_state == "not_started":
            self.set_start_button("Start", (31, 106, 165), True)

    def check_lol_settings(self):
        if (
            GetLolSettings.observer is None
            and os.path.exists(get_lol_settings_path())
            and os.path.exists(get_game_cfg_path())
        ):
            GetLolSettings.start()

    def check_game_status(self):
        if is_game_active():
            self.handle_active_game()
        elif self.start_state not in ("not_started", "started"):
            self.start_state = "not_started"

    def handle_active_game(self):
        if LolWindowData.get_window_mode() != 2:
            self.set_error_state(
                "window_mode_error", "LoL must be in borderless window mode!"
            )
        elif GameData.get_game_mode() not in ("CLASSIC", "ARAM", "PRACTICETOOL"):
            self.set_error_state("game_mode_error", "Not playable in this game mode!")
        elif ActivePlayerData.get_champion_name() == "Aphelios":
            self.set_error_state("champion_error", "Not playable with Aphelios!")
        elif self.start_state == "started":
            self.hide()
            self.main_loop_timer.stop()
            SettingsManager.update(self.ui)
            MainManager.start_game()
        else:
            self.start_state = "not_started"

    def set_error_state(self, error_state: str, info_text: str):
        self.start_state = error_state
        self.set_start_button("N/A", (52, 54, 56))
        self.ui.info_label.setText(info_text)
        self.ui.info_label.show()

    # events
    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        self.main_loop_timer.stop()

        self.stop_window.close()
        self.game_overlay.close()
        self.quest_display.close()
        self.hide()

        MainManager.stop_program()

        QApplication.quit()

    # utils
    def set_start_button(self, text: str, color: tuple, enable: bool = False):
        start_button = self.ui.start_button
        start_button.setText(text)
        start_button.setStyleSheet(
            "QPushButton{\n"
            "color: rgb(235, 235, 235);\n"
            f"background-color: rgb{color};\n"
            "border-radius: 5px\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color: rgb(20, 72, 112);\n"
            "}"
        )

        start_button.setEnabled(enable)

        self.ui.info_label.hide()


def create_main_menu():
    global main_menu
    main_menu = MainMenu()


def get_main_menu():
    return main_menu
