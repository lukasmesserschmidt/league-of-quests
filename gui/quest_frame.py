from PySide6.QtWidgets import QFrame
from PySide6.QtCore import QTimer

from .quest_frame_base import Ui_QuestFrame
from ..quests.quest_base import QuestBase
from ..restrictions.restriction_base import RestrictionBase
from ..utils.time import convert_time


class QuestFrame(QFrame):
    def __init__(self, quest, restriction):
        super().__init__()
        self.quest: QuestBase
        self.quest = quest
        self.restriction: RestrictionBase
        self.restriction = restriction

        self.ui = Ui_QuestFrame()
        self.ui.setupUi(self)

        self.set_quest_title()
        self.set_restriction_title()

        self.main_loop_timer = QTimer(self)
        self.main_loop_timer.timeout.connect(self.main_loop)
        self.main_loop_timer.start(100)

    def set_quest_title(self):
        self.ui.title_label.setText(self.quest.title)

    def set_restriction_title(self):
        self.ui.restriction_label.setText(self.restriction.title)

    def main_loop(self):
        self.update_quest_time()

        if self.quest.update_title:
            self.set_quest_title()

        if self.quest.finish_color_enabled:
            self.change_timer_color((13, 219, 13))
        else:
            self.change_timer_color((235, 235, 235))

    def update_quest_time(self):
        text = convert_time(self.quest.remaining_time)
        self.ui.time_label.setText(text)

    def change_timer_color(self, color: tuple):
        self.ui.time_label.setStyleSheet(
            f"background-color: rgb{color};\n" "border-radius:5px\n" "\n" ""
        )
