from PySide6.QtWidgets import QFrame

from .quest_display_frame_base import Ui_QuestDisplayFrame


class QuestDisplayFrame(QFrame):
    def __init__(self):
        super().__init__()

        self.frame = Ui_QuestDisplayFrame()
        self.frame.setupUi(self)
