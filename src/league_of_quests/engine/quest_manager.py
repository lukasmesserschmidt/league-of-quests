import time
from threading import Thread

from .quest_creator import QuestCreator
from ..data import (
    LiveClientDataFetcher,
    LiveClientConfigMonitor,
    ConfigFetcher,
    Config,
    QuestState,
)
from ..game import GameDisruptor, GameContext
from ..content.quests.base import Quest


class QuestManager:
    def __init__(self):
        self.active_quests: list[Quest] = []
        self.live_client_data_fetcher = LiveClientDataFetcher()
        self.live_client_config_monitor = LiveClientConfigMonitor()
        self.game_disruptor = GameDisruptor()
        self.config_fetcher = ConfigFetcher()
        self.quest_creator = QuestCreator(self.config_fetcher)

    def start(self):
        """Start the quest manager loop in a separate thread."""
        Thread(target=self._loop, daemon=True).start()

    def _loop(self):
        config = self.config_fetcher.fetch()

        last_time = None
        last_quest_creation_time = None
        last_player_deaths = None
        while True:
            # Fetch live client data and live client config
            live_client_data = self.live_client_data_fetcher.fetch()
            live_client_config = self.live_client_config_monitor.get_config()
            if live_client_data is None or live_client_config is None:
                continue

            # Create a GameContext from the fetched live client data and live client config
            game_context = GameContext(live_client_data, live_client_config)

            game_time = game_context.get_data().gameData.gameTime

            if last_time is None:
                # If this is the first time the loop is run, set the last time
                last_time = game_time
                last_quest_creation_time = game_time

            dt = game_time - last_time
            last_time = game_time

            # Update all active quests
            for quest in self.active_quests:
                quest.update(dt, game_context)

                # Print quest information
                print("--------------------------------------------------")
                print(f"Quest Description: {quest.get_description()}")
                print(f"Time Left: {quest.get_time_left()}")
                print(f"Current Value: {quest.get_progress()}")
                print(f"Goal: {quest.get_goal()}")
                print(f"Quest: {quest.__class__.__name__}")
                print(f"State: {quest.get_state()}")

                print()

                restriction = quest.get_restriction()
                print(f"Restriction Description: {restriction.get_description()}")
                print(f"Restriction: {restriction.__class__.__name__}")
                print(f"Current Hotkeys: {self.game_disruptor._current_hotkeys}")

                # Check if a quest has completed or failed
                if quest.get_state() in (QuestState.COMPLETED, QuestState.FAILED):
                    quest.stop()
                    self._remove_quest(quest)

                    # If a quest has failed and the config allows it, create a new quest
                    if quest.get_state() == QuestState.FAILED and config.quests.new_quest_on_fail:
                        self._try_add_quest(game_context, config)

                    continue

            # Check if it's time to create a new quest based on time
            if config.quests.new_quest_after_time:
                time_since_last_quest = game_time - last_quest_creation_time
                if time_since_last_quest >= config.quests.new_quest_after_time_interval:
                    self._try_add_quest(game_context, config)
                    last_quest_creation_time = game_time

            # Check player died and add quest if new quest on death is enabled
            if config.quests.new_quest_on_death:
                current_deaths = self._get_player_deaths(game_context)
                if last_player_deaths is None:
                    last_player_deaths = current_deaths
                elif current_deaths is not None:
                    if current_deaths > last_player_deaths:
                        self._try_add_quest(game_context, config)
                        last_player_deaths = current_deaths

            # Delay before the next iteration of the loop
            time.sleep(0.5)

    def _get_player_deaths(self, game_context: GameContext):
        """Get the number of deaths for the active player."""
        riotId = game_context.get_data().activePlayer.riotId
        all_players = game_context.get_data().allPlayers
        for player in all_players:
            if player.riotId == riotId:
                return player.scores.deaths
        return None

    def _add_quest(self, game_context: GameContext):
        """Add a new quest to the active quests list."""
        quest = self.quest_creator.create_quest(
            self.active_quests, game_context, self.game_disruptor
        )
        self.active_quests.append(quest)
        return quest

    def _try_add_quest(self, game_context: GameContext, config: Config):
        """Try to add a new quest if the limit has not been reached."""
        if len(self.active_quests) < config.quests.limit:
            quest = self._add_quest(game_context)
            quest.start(game_context)

    def _remove_quest(self, quest: Quest):
        """Remove a quest from the active quests list."""
        self.active_quests.remove(quest)
