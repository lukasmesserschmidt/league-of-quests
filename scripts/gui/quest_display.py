"""
This module contains the QuestDisplay class, 
which displays the quests, quest timer and quest count in the game overlay.
"""

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QCursor
from pynput import mouse

from .window_base import WindowBase
from .quest_display_ui import QuestDisplayUi
from ..manager.settings_manager import SettingsManager
from ..lol_data.lol_settings import LolSettings
from ..lol_data.lol_window_data import LolWindowData
from ..utils import user_data
from ..utils.game_overlay_scaling import get_map_size
from ..utils.is_game_active import is_game_active
from ..utils.is_program_active import is_program_active
from ..utils.constants import Constants


class QuestDisplay(WindowBase):
    """
    A class for displaying the quests, quest timer and quest count in the game overlay.
    """

    def __init__(self):
        super().__init__()

        # set window attributes
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint
            | Qt.WindowTransparentForInput
            | Qt.FramelessWindowHint
        )

        # setup ui
        self.ui = QuestDisplayUi()
        self.ui.setupUi(self)

        # init variables
        self._start_x_diff = 0
        self._start_y_diff = 0
        self._last_width = self.geometry().width()
        self.is_dragging = False

        self._mouse_listener = None

        # update loop
        self._update_loop_timer = QTimer(self)
        self._update_loop_timer.timeout.connect(self._update_loop)

        self.hide()

    def start(self):
        """
        Moves the quest display to the default position and start the quest display update loop.
        """
        self._move_default_pos()
        self._mouse_listener = mouse.Listener(on_click=self._on_click)
        self._mouse_listener.start()
        self._update_loop_timer.start(10)

    def stop(self):
        """
        Stop the quest display update loop and hide the quest display.
        """
        self._update_loop_timer.stop()
        if self._mouse_listener is not None:
            self._mouse_listener.stop()
        self.hide()

    def _move_default_pos(self):
        x, y = user_data.get_monitor_dpi_resolution()
        map_size = get_map_size()
        space = get_map_size() * 0.05
        x -= (
            (map_size + space)
            if not LolSettings.get_lol_setting(Constants.FLIP_MAP)
            else 0
        ) + 250
        y -= 300

        self.move(x, y)

    def _update_loop(self):
        self._move_to_mouse()
        self._stretch_to_left()

        if is_program_active() and is_game_active() and LolWindowData.lol_is_top:
            self.show()
            self.raise_()
        else:
            self.hide()

    def _on_click(self, x, y, button, pressed):
        mouse_x, mouse_y = QCursor.pos().toTuple()
        left_x, top_y = self.geometry().topLeft().toTuple()
        right_x, bottom_y = self.geometry().bottomRight().toTuple()
        if (
            pressed
            and button == mouse.Button.left
            and left_x < mouse_x < right_x
            and top_y < mouse_y < bottom_y
        ):

            self._start_x_diff = mouse_x - left_x
            self._start_y_diff = mouse_y - top_y

            self.is_dragging = True
        else:
            self.is_dragging = False

    def _move_to_mouse(self):
        if self.is_dragging:
            mouse_x, mouse_y = QCursor.pos().toTuple()
            x = mouse_x - self._start_x_diff
            y = mouse_y - self._start_y_diff
            self.move(x, y)

    def _stretch_to_left(self):
        current_width = self.geometry().width()
        if current_width != self._last_width:
            width_diff = current_width - self._last_width
            x = self.geometry().left() - width_diff
            y = self.geometry().top()

            self.move(x, y)
            self._last_width = current_width

    def get_timer_text(self):
        """
        Returns the text displayed in the next quest time label.
        """
        return self.ui.next_quest_time_label.text()

    def set_timer_text(self, text: str):
        """
        Sets the text of the next quest time label ot the given text.
        """
        self.ui.next_quest_time_label.setText(text)

    def get_quest_count(self):
        """
        Returns the text displayed in the quest count label.
        """
        return self.ui.quest_count_label.text()

    def set_quest_count(self, count: int):
        """
        Sets the text of the quest count label to the given count.
        """
        self.ui.quest_count_label.setText(
            f"{count}/{SettingsManager.get_quest_limit()}"
        )

    def add_widget(self, widget: QWidget):
        """
        Adds a widget to the quest frame layout.
        """
        self.ui.quest_frame_layout.addWidget(widget, 1, Qt.AlignRight | Qt.AlignTop)
