from PySide6.QtCore import Qt, QFile, QIODevice, QTimer
from PySide6.QtUiTools import QUiLoader

from .quest_frame import QuestFrame
from ..data import ConfigFetcher, QuestState


class GameWindow:
    def __init__(self):
        super().__init__()

        file = QFile(
            "C:\\dev\\league-of-quests\\src\\league_of_quests\\ui\\ui_files\\game_window.ui"
        )
        file.open(QIODevice.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file)
        file.close()

        self.ui.move(0, 0)

        self.ui.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.Tool
            | Qt.WindowTransparentForInput
        )
        self.ui.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.setAttribute(Qt.WA_ShowWithoutActivating)

        self.config_fetcher = ConfigFetcher()

        self._quest_frames: dict[int, QuestFrame] = {}

        self.ui.show()

    def update(self, time_to_next_quest: float, quest_scores: dict[QuestState, int]):
        config = self.config_fetcher.fetch()

        self.ui.quest_count_label.setText(f"{len(self._quest_frames)}/{config.quests.limit}")

        if config.quests.new_quest_after_time:
            self.ui.next_quest_time_label.setText(
                f"{int(time_to_next_quest // 60):02d}:{int(time_to_next_quest % 60):02d}"
            )
        else:
            self.ui.next_quest_time_label.setText("")

        self.ui.quest_scores_label.setText(
            f"{quest_scores[QuestState.COMPLETED]} | {quest_scores[QuestState.FAILED]}"
        )

    def add_quest_frame(self, quest_id: int, quest_frame: QuestFrame):
        index = self.ui.vertical_layout.count() - 1
        self.ui.vertical_layout.insertWidget(index, quest_frame.ui)
        self._quest_frames[quest_id] = quest_frame

    def remove_quest_frame(self, quest_id: int):
        if quest_id in self._quest_frames:
            quest_frame = self._quest_frames.pop(quest_id)
            QTimer.singleShot(1000, lambda: quest_frame.ui.deleteLater())

    def update_quest_frame(
        self, quest_id: int, time_left: float, progress: float, goal: float, state: QuestState
    ):
        if quest_id in self._quest_frames:
            self._quest_frames[quest_id].update(time_left, progress, goal, state)
