import time

from .quest_creator import QuestCreator
from ..data import LiveClientDataFetcher
from ..data import LiveClientConfigMonitor
from ..core import GameDisruptor
from ..core import GameContext
from ..core import QuestState
from ..core.quests import Quest


class QuestManager:
    def __init__(self):
        self.active_quests: list[Quest] = []
        self.live_client_data_fetcher = LiveClientDataFetcher()
        self.quest_creator = QuestCreator()
        self.live_client_config_monitor = LiveClientConfigMonitor()
        self.game_disruptor = GameDisruptor(self.live_client_config_monitor)

    def loop(self):
        last_time = None
        while True:
            live_client_data = self.live_client_data_fetcher.fetch()
            live_client_config = self.live_client_config_monitor.get_config()
            if live_client_data is None or live_client_config is None:
                continue

            game_context = GameContext(live_client_data, live_client_config)

            t = game_context.get_live_client_data().gameData.gameTime

            if last_time is None:
                last_time = t
                # test
                quest = self._create_quest(game_context)
                quest.start(game_context)

            dt = t - last_time
            last_time = t

            for quest in self.active_quests:
                quest.update(dt, game_context)

                if (
                    quest.get_state() == QuestState.COMPLETED
                    or quest.get_state() == QuestState.FAILED
                ):
                    quest.stop()
                    self._remove_quest(quest)
                    continue

                print("-----")
                print(f"State: {quest.get_state()}")
                print(f"Time Left: {quest.get_time_left()}")
                print(f"Current Value: {quest.get_progress()}")
                print(f"Goal: {quest.get_goal()}")

                restriction = quest.get_restriction()
                print(f"Restriction: {restriction.__class__.__name__}")
                print(f"Restriction Description: {restriction.description}")

            time.sleep(1)

    def _create_quest(self, game_context):
        quest = self.quest_creator.create_quest(
            self.active_quests, game_context, self.game_disruptor
        )
        self.active_quests.append(quest)
        return quest

    def _remove_quest(self, quest):
        self.active_quests.remove(quest)
        return quest
