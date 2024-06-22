"""
This module contains the StopWindow class.
"""

from PySide6.QtCore import QTimer
from PySide6.QtCore import Signal

from .window_base import WindowBase
from .stop_window_ui import StopWindowUi
from ..utils.is_game_active import is_game_active


class StopWindow(WindowBase):
    """
    The stop window while the game is running.
    """

    # signals
    stoped = Signal()

    def __init__(self):
        super().__init__()

        # setup ui
        self.ui = StopWindowUi()
        self.ui.setupUi(self)

        # config
        self._config_widgets()

        # update loop
        self._update_loop_timer = QTimer(self)
        self._update_loop_timer.timeout.connect(self._update_loop)

        self.hide()

    # config
    def _config_widgets(self):
        self.ui.stop_button.clicked.connect(self._stop_command)

    def _stop_command(self):
        self.stop()
        self.stoped.emit()

    # control
    def start(self):
        """
        Starts the stop window by showing it and starting the update loop timer.
        """
        self.show()
        self._update_loop_timer.start(500)

    def stop(self):
        """
        Hides the stop window and stops the update loop timer.
        """
        self.hide()
        self._update_loop_timer.stop()

    # update loop
    def _update_loop(self):
        if not is_game_active():
            self._stop_command()
