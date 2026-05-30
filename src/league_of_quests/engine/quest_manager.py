import time

from ..data import LiveClientDataFetcher
from ..content.quests import GetStatQuest, GetLevelQuest
from ..core.states import Difficulty


class QuestManager:
    def __init__(self):
        self.active_quests = []
        self.live_client_data_fetcher = LiveClientDataFetcher()

    def loop(self):
        quest = GetStatQuest(None)

        last_time = None
        while True:
            live_client_data = self.live_client_data_fetcher.fetch()
            if live_client_data is None:
                continue

            t = live_client_data.gameData.gameTime

            if last_time is None:
                last_time = t
                quest.start(live_client_data)

            dt = t - last_time
            last_time = t

            quest.update(dt, live_client_data)

            # print completed, failed, holding, time left, holding timer, stat value each on a new line
            print("-----")
            print(f"State: {quest.get_state()}")
            print(f"Time Left: {quest.get_time_left()}")
            print(f"Current Value: {quest.get_progress()}")
            print(f"Goal: {quest.get_goal()}")

            time.sleep(1)
