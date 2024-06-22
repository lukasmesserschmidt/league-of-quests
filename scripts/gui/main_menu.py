"""
This module contains the MainMenu class, which is the main window of the program.
"""

import os
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtGui import QCloseEvent

from .main_menu_ui import MainWindowUi
from .quest_display import QuestDisplay
from .game_overlay.game_overlay_window import GameOverlayWindow
from .stop_window import StopWindow
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
    """
    The main window of the program.
    """

    def __init__(self):
        super().__init__()

        # setup ui
        self.ui = MainWindowUi()
        self.ui.setupUi(self)

        # get windows
        self._stop_window = StopWindow.get_instance()
        self._quest_display = QuestDisplay.get_instance()
        self._game_overlay = GameOverlayWindow.get_instance()

        # config
        self._config_widgets()

        # update loop
        self._start_state = None

        self._update_loop_timer = QTimer(self)
        self._update_loop_timer.timeout.connect(self._update_loop)

        # flags
        self._has_shown_any_combination_warning = False

        # start
        if is_lol_installed():
            self._start()
        else:
            self._set_start_button("N/A", (52, 54, 56))
            self.ui.info_label.setText(
                "League of Legends is not installed\n(install League of Legends and restart)!"
            )
            self.ui.info_label.show()

        self.show()

    # config
    def _config_widgets(self):
        # checkboxes
        self.ui.quest_on_death_checkbox.stateChanged.connect(
            lambda state: self._set_checkbox(self.ui.quest_after_time_checkbox, state)
        )

        self.ui.quest_after_time_checkbox.stateChanged.connect(
            lambda state: self._set_checkbox(self.ui.quest_on_death_checkbox, state)
        )

        self.ui.allow_similar_checkbox.stateChanged.connect(
            self._show_any_combination_warning
        )

        # start button
        self.ui.start_button.clicked.connect(self._start_button_command)

        # connections
        self._stop_window.closed.connect(self.close)
        self._stop_window.stoped.connect(self._stop_game)

        self._quest_display.closed.connect(self.close)

        self._game_overlay.closed.connect(self.close)

    def _set_checkbox(self, checkbox, state):
        if state is False:
            checkbox.setChecked(True)

    def _show_any_combination_warning(self, state):
        if not self._has_shown_any_combination_warning and state:
            self._show_popup(
                "Warning!",
                "This setting allows any quest/restriction combination, which can lead to unexpected behavior as it is not designed for this purpose. Please use with caution.",
            )
            self._has_shown_any_combination_warning = True

    def _start_button_command(self):
        self._start_state = (
            "started" if self._start_state == "not_started" else "not_started"
        )
        self._update_start_button()

    # control
    def _start(self):
        self._start_state = "not_started"
        self._set_start_button("Start", (31, 106, 165), True)
        self._update_loop_timer.start(100)
        self.show()

    def _stop_game(self):
        MainManager.stop_game()
        self._start()

    # update loop
    def _update_loop(self):
        self._update_start_button()
        self._check_lol_settings()
        self._check_game_status()

    def _update_start_button(self):
        if self._start_state == "started":
            self._set_start_button("Waiting", (52, 54, 56), True)
        elif self._start_state == "not_started":
            self._set_start_button("Start", (31, 106, 165), True)

    def _check_lol_settings(self):
        if (
            GetLolSettings.observer is None
            and os.path.exists(get_lol_settings_path())
            and os.path.exists(get_game_cfg_path())
        ):
            GetLolSettings.start()

    def _check_game_status(self):
        if is_game_active():
            self._handle_active_game()
        elif self._start_state not in ("not_started", "started"):
            self._start_state = "not_started"

    def _handle_active_game(self):
        if LolWindowData.get_window_mode() != 2:
            self._set_error_state(
                "window_mode_error", "LoL must be in borderless window mode!"
            )
        elif GameData.get_game_mode() not in ("CLASSIC", "ARAM", "PRACTICETOOL"):
            self._set_error_state("game_mode_error", "Not playable in this game mode!")
        elif ActivePlayerData.get_champion_name() == "Aphelios":
            self._set_error_state("champion_error", "Not playable with Aphelios!")
        elif self._start_state == "started":
            self.hide()
            self._update_loop_timer.stop()
            SettingsManager.update(self.ui)
            MainManager.start_game()
        else:
            self._start_state = "not_started"

    def _set_error_state(self, error_state: str, info_text: str):
        self._start_state = error_state
        self._set_start_button("N/A", (52, 54, 56))
        self.ui.info_label.setText(info_text)
        self.ui.info_label.show()

    # events
    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        self._update_loop_timer.stop()

        self._stop_window.close()
        self._game_overlay.close()
        self._quest_display.close()
        self.hide()

        MainManager.stop_program()

        QApplication.quit()

    # utils
    def _set_start_button(self, text: str, color: tuple, enable: bool = False):
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

    def _show_popup(self, title: str, message: str):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
