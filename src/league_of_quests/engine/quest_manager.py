import time

from .quest_creator import QuestCreator
from ..data import LiveClientDataFetcher
from ..data import LiveClientConfigMonitor
from ..data import ConfigFetcher
from ..core import GameDisruptor
from ..core import GameContext
from ..core import QuestState
from ..core.quests import Quest


class QuestManager:
    def __init__(self):
        self.active_quests: list[Quest] = []
        self.live_client_data_fetcher = LiveClientDataFetcher()
        self.live_client_config_monitor = LiveClientConfigMonitor()
        self.game_disruptor = GameDisruptor(self.live_client_config_monitor)
        self.config_fetcher = ConfigFetcher()
        self.quest_creator = QuestCreator(self.config_fetcher)

    def start(self):
        self._loop()

    def _loop(self):
        config = self.config_fetcher.fetch()

        last_time = None
        last_quest_creation_time = None
        while True:
            # Fetch live client data and live client config
            live_client_data = self.live_client_data_fetcher.fetch()
            live_client_config = self.live_client_config_monitor.get_config()
            if live_client_data is None or live_client_config is None:
                continue

            # Create a GameContext from the fetched live client data and live client config
            game_context = GameContext(live_client_data, live_client_config)

            game_time = game_context.get_live_client_data().gameData.gameTime

            if last_time is None:
                # If this is the first time the loop is run, set the last time
                last_time = game_time
                last_quest_creation_time = game_time
                # Test: create a quest immediately
                quest = self._add_quest(game_context)
                quest.start(game_context)

            dt = game_time - last_time
            last_time = game_time

            # Update all active quests
            for quest in self.active_quests:
                quest.update(dt, game_context)

                # Check if a quest has completed or failed
                if quest.get_state() in (QuestState.COMPLETED, QuestState.FAILED):
                    quest.stop()
                    self._remove_quest(quest)

                    # If a quest has failed and the config allows it, create a new quest
                    if quest.get_state() == QuestState.FAILED and config.quests.new_quest_on_fail:
                        self._try_add_quest(game_context, config)

                    continue

                # Print quest information
                print("--------------------------------------------------")
                print(f"Quest Description: {quest.description}")
                print(f"Time Left: {quest.get_time_left()}")
                print(f"Current Value: {quest.get_progress()}")
                print(f"Goal: {quest.get_goal()}")
                print(f"Quest: {quest.__class__.__name__}")
                print(f"State: {quest.get_state()}")

                print()

                restriction = quest.get_restriction()
                print(f"Restriction Description: {restriction.description}")
                print(f"Restriction: {restriction.__class__.__name__}")
                print(f"Current Hotkeys: {self.game_disruptor._current_hotkeys}")

            # Check if it's time to create a new quest based on time
            if config.quests.new_quest_after_time:
                time_since_last_quest = game_time - last_quest_creation_time
                if time_since_last_quest >= config.quests.new_quest_after_time_interval:
                    self._try_add_quest(game_context, config)
                    last_quest_creation_time = game_time

            # Delay before the next iteration of the loop
            time.sleep(0.5)

    def _add_quest(self, game_context):
        """Add a new quest to the active quests list."""
        quest = self.quest_creator.create_quest(
            self.active_quests, game_context, self.game_disruptor
        )
        self.active_quests.append(quest)
        return quest

    def _try_add_quest(self, game_context, config):
        """Try to add a new quest if the limit has not been reached."""
        if len(self.active_quests) < config.quests.limit:
            quest = self._add_quest(game_context)
            quest.start(game_context)

    def _remove_quest(self, quest):
        """Remove a quest from the active quests list."""
        self.active_quests.remove(quest)
