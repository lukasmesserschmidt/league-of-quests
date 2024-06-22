"""
This module contains the QuestFrame class, which displays the quest frame in the quest display.
"""

from PySide6.QtWidgets import QFrame
from PySide6.QtCore import QTimer

from .quest_frame_ui import QuestFrameUi
from ..quests.quest_base import QuestBase
from ..restrictions.restriction_base import RestrictionBase
from ..utils.time import convert_time


class QuestFrame(QFrame):
    """
    A class for displaying the quest frame in the quest display.
    """

    def __init__(self, quest: QuestBase, restriction: RestrictionBase):
        super().__init__()

        # init variables
        self.quest = quest
        self.restriction = restriction

        # setup ui
        self.ui = QuestFrameUi()
        self.ui.setupUi(self)

        # init titles
        self._set_quest_title()
        self._set_restriction_title()

        # update loop
        self._update_loop_timer = QTimer(self)
        self._update_loop_timer.timeout.connect(self._update_loop)
        self._update_loop_timer.start(500)

    # update loop
    def _update_loop(self):
        if not self.quest.quest_complete:
            self._update_quest_time()

            if self.quest.update_title:
                self._set_quest_title()

            if self.quest.finish_color_enabled:
                self._change_timer_color((13, 219, 13))
            else:
                self._change_timer_color((235, 235, 235))

    # utils
    def _set_quest_title(self):
        self.ui.title_label.setText(self.quest.title)

    def _set_restriction_title(self):
        self.ui.restriction_label.setText(self.restriction.title)

    def _update_quest_time(self):
        time = convert_time(self.quest.remaining_time)
        self.ui.time_label.setText(time)

    def _change_timer_color(self, color: tuple[int, int, int]):
        self.ui.time_label.setStyleSheet(
            f"background-color: rgb{color};\n" "border-radius:5px"
        )

    # events
    def deleteLater(self):
        """
        Stops the update loop timer and deletes the quest frame.
        """
        self._update_loop_timer.stop()
        super().deleteLater()
