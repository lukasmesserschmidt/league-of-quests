from PySide6.QtCore import QObject, Signal
import time

from ..data import LiveClientDataFetcher, LiveClientData


class GameWatcher(QObject):
    game_started = Signal(LiveClientData)
    game_ended = Signal()
    data_updated = Signal(LiveClientData)

    def __init__(self):
        super().__init__()
        self._live_client_data_fetcher = LiveClientDataFetcher()
        self._running = True

    def stop(self):
        self._running = False

    def run(self):
        in_game = False
        while self._running:
            live_client_data = self._live_client_data_fetcher.fetch()
            if live_client_data:
                if not in_game:
                    in_game = True
                    self.game_started.emit(live_client_data)

                if in_game:
                    self.data_updated.emit(live_client_data)
            elif in_game:
                in_game = False
                self.game_ended.emit()

            time.sleep(0.5)
