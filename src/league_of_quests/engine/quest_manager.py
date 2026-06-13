from PySide6.QtCore import QObject, Signal

from .quest_creator import QuestCreator
from ..data import (
    LiveClientConfigFetcher,
    ConfigFetcher,
    LiveClientData,
    Config,
    QuestState,
)
from ..game import GameDisruptor, GameContext
from ..content.quests.base import Quest


class QuestManager(QObject):
    quest_added = Signal(Quest)
    quest_removed = Signal(Quest)
    quest_updated = Signal(Quest)

    def __init__(self, game_disruptor: GameDisruptor):
        super().__init__()
        self.live_client_config_fetcher = LiveClientConfigFetcher()
        self.config_fetcher = ConfigFetcher()
        self.quest_creator = QuestCreator(self.config_fetcher)

        self.game_disruptor = game_disruptor

        self._active_quests: list[Quest] = []
        self._quest_scores: dict[QuestState, int] = {QuestState.COMPLETED: 0, QuestState.FAILED: 0}

    def get_quest_scores(self) -> dict[QuestState, int]:
        return self._quest_scores

    def get_time_to_next_quest(self):
        return (
            self._last_quest_creation_time
            + self.config_fetcher.fetch().quests.new_quest_after_time_interval
            - self._last_time
        )

    def start(self, live_client_data: LiveClientData):
        game_time = live_client_data.gameData.gameTime
        self._last_time = game_time
        self._last_quest_creation_time = game_time
        self._last_player_deaths = self._get_player_deaths(live_client_data)

    def update(self, live_client_data: LiveClientData):
        config = self.config_fetcher.fetch()

        # Fetch live client data and live client config
        live_client_config = self.live_client_config_fetcher.fetch()
        if live_client_config is None:
            return

        # Create a GameContext from the fetched live client data and live client config
        game_context = GameContext(live_client_data, live_client_config)

        game_time = game_context.get_data().gameData.gameTime

        dt = game_time - self._last_time
        self._last_time = game_time

        # Update all active quests
        for quest in self._active_quests:
            quest.update(dt, game_context)
            self.quest_updated.emit(quest)

            # Check if a quest has completed or failed
            if quest.get_state() in (QuestState.COMPLETED, QuestState.FAILED):
                quest.stop()
                self._remove_quest(quest)
                self._quest_scores[quest.get_state()] += 1

                # If a quest has failed and the config allows it, create a new quest
                if quest.get_state() == QuestState.FAILED and config.quests.new_quest_on_fail:
                    self._try_add_quest(game_context, config)

                continue

        # Check if it's time to create a new quest based on time
        if config.quests.new_quest_after_time:
            time_since_last_quest = game_time - self._last_quest_creation_time
            if time_since_last_quest >= config.quests.new_quest_after_time_interval:
                self._try_add_quest(game_context, config)
                self._last_quest_creation_time = game_time

        # Check player died and add quest if new quest on death is enabled
        if config.quests.new_quest_on_death:
            current_deaths = self._get_player_deaths(live_client_data)
            if self._last_player_deaths is None:
                self._last_player_deaths = current_deaths
            elif current_deaths is not None and current_deaths > self._last_player_deaths:
                self._try_add_quest(game_context, config)
                self._last_player_deaths = current_deaths

    def _get_player_deaths(self, live_client_data: LiveClientData):
        """Get the number of deaths for the active player."""
        riotId = live_client_data.activePlayer.riotId
        all_players = live_client_data.allPlayers
        for player in all_players:
            if player.riotId == riotId:
                return player.scores.deaths
        return None

    def _try_add_quest(self, game_context: GameContext, config: Config):
        """Try to add a new quest if the limit has not been reached."""
        if len(self._active_quests) < config.quests.limit:
            self._add_quest(game_context)

    def _add_quest(self, game_context: GameContext):
        """Add a new quest to the active quests dict."""
        quest = self.quest_creator.create_quest(
            self._active_quests, game_context, self.game_disruptor
        )
        self._active_quests.append(quest)
        quest.start(game_context)
        self.quest_added.emit(quest)

    def _remove_quest(self, quest: Quest):
        """Remove a quest from the active quests dict."""
        if quest not in self._active_quests:
            return

        self._active_quests.remove(quest)
        self.quest_removed.emit(quest)
