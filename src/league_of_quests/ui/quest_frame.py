from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader

from ..data import Difficulty, QuestState


class QuestFrame:
    def __init__(
        self,
        quest_description: str,
        restriction_description: str,
        quest_difficulty: Difficulty,
        restriction_difficulty: Difficulty,
    ):
        file = QFile(
            "C:\\dev\\league-of-quests\\src\\league_of_quests\\ui\\ui_files\\quest_frame.ui"
        )
        file.open(QIODevice.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file)
        file.close()

        self.ui.quest_label.setText(f"   {quest_description}")
        self.ui.restriction_label.setText(f"   {restriction_description}")

        if quest_difficulty == Difficulty.EASY:
            self._set_quest_color(0, 255, 0)
        elif quest_difficulty == Difficulty.MEDIUM:
            self._set_quest_color(255, 255, 0)
        elif quest_difficulty == Difficulty.HARD:
            self._set_quest_color(255, 0, 0)

        if restriction_difficulty == Difficulty.EASY:
            self._set_restriction_color(0, 255, 0)
        elif restriction_difficulty == Difficulty.MEDIUM:
            self._set_restriction_color(255, 255, 0)
        elif restriction_difficulty == Difficulty.HARD:
            self._set_restriction_color(255, 0, 0)

        self.ui.show()

    def update(self, time_left: float, progress: float, goal: float, state: QuestState):
        self.ui.time_label.setText(f"{int(time_left // 60):02d}:{int(time_left % 60):02d}")
        self.ui.progress_label.setText(f"{int(progress)}/{int(goal)}")

        if state == QuestState.CONDITION_NOT_MET:
            self._set_state_color(40, 40, 40)
        elif state == QuestState.CONDITION_MET:
            self._set_state_color(0, 0, 80)
        elif state == QuestState.COMPLETED:
            self._set_state_color(0, 80, 0)
        elif state == QuestState.FAILED:
            self._set_state_color(80, 0, 0)

    def _set_state_color(self, r: int, g: int, b: int):
        style = f"""
            #score_frame {{
            background-color: rgba({r}, {g}, {b}, 0.5);
            border-top-left-radius: 8px;
            border-bottom-left-radius: 8px;
            }}
        """

        self.ui.score_frame.setStyleSheet(style)

    def _set_quest_color(self, r: int, g: int, b: int):
        style = f"""
            #quest_label {{
            color: rgba(255, 255, 255, 0.8);
            background-color: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 rgba({r}, {g}, {b}, 0.1),
                stop: 1 rgba({r}, {g}, {b}, 0.0)
            );
            border-top-right-radius: 8px;
            }}
        """

        self.ui.quest_label.setStyleSheet(style)

    def _set_restriction_color(self, r: int, g: int, b: int):
        style = f"""
            #restriction_label {{
            color: rgba(255, 255, 255, 0.7);
            background-color: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 rgba({r}, {g}, {b}, 0.1),
                stop: 1 rgba({r}, {g}, {b}, 0.0)
            );
            border-top-right-radius: 8px;
            }}
        """

        self.ui.restriction_label.setStyleSheet(style)
