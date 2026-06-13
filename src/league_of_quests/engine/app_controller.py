from PySide6.QtCore import QObject, QThread, Slot

from .quest_manager import QuestManager
from ..content import Quest
from ..ui import MainWindow, GameWindow, GameOverlayWindow, QuestFrame
from ..game import GameWatcher, GameDisruptor, GameOverlay
from ..data import LiveClientData


class AppController(QObject):
    def __init__(self):
        super().__init__()

        self.main_window = MainWindow()
        self.game_window = None
        self.game_overlay_window = None

        self.quest_manager = None

        self.watcher_thread = QThread()
        self.watcher = GameWatcher()
        self.watcher.moveToThread(self.watcher_thread)

        self.watcher_thread.started.connect(self.watcher.run)
        self.watcher.game_started.connect(self.handle_game_started)
        self.watcher.game_ended.connect(self.handle_game_ended)
        self.watcher.data_updated.connect(self.handle_data_updated)

        self.watcher_thread.start()

        self.main_window.ui.show()

    @Slot(LiveClientData)
    def handle_game_started(self, live_client_data: LiveClientData):
        self.game_window = GameWindow()
        self.game_overlay_window = GameOverlayWindow()

        game_overlay = GameOverlay(self.game_overlay_window)
        game_disruptor = GameDisruptor(game_overlay)
        self.quest_manager = QuestManager(game_disruptor)

        self.quest_manager.quest_added.connect(self.handle_quest_added)
        self.quest_manager.quest_removed.connect(self.handle_quest_removed)
        self.quest_manager.quest_updated.connect(self.handle_quest_updated)

        self.game_window.ui.show()
        self.game_overlay_window.show()
        self.quest_manager.start(live_client_data)

    @Slot()
    def handle_game_ended(self):
        self.quest_manager = None

        if self.game_window:
            self.game_window.ui.close()
            self.game_window = None

        if self.game_overlay_window:
            self.game_overlay_window.close()
            self.game_overlay_window = None

    @Slot(LiveClientData)
    def handle_data_updated(self, live_client_data: LiveClientData):
        if not self.quest_manager or not self.game_window:
            return

        self.quest_manager.update(live_client_data)

        time_to_next_quest = self.quest_manager.get_time_to_next_quest()
        quest_scores = self.quest_manager.get_quest_scores()
        self.game_window.update(time_to_next_quest, quest_scores)

    @Slot(Quest)
    def handle_quest_added(self, quest: Quest):
        if self.game_window:
            restriction = quest.get_restriction()
            quest_frame = QuestFrame(
                quest.get_description(),
                restriction.get_description(),
                quest.difficulty,
                restriction.difficulty,
            )
            self.game_window.add_quest_frame(quest.get_id(), quest_frame)

    @Slot(Quest)
    def handle_quest_removed(self, quest: Quest):
        if self.game_window:
            self.game_window.remove_quest_frame(quest.get_id())

    @Slot(Quest)
    def handle_quest_updated(self, quest: Quest):
        if self.game_window:
            self.game_window.update_quest_frame(
                quest.get_id(),
                quest.get_time_left(),
                quest.get_progress(),
                quest.get_goal(),
                quest.get_state(),
            )
