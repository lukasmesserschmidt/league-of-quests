import time

from ..data import LiveClientDataFetcher
from ..data import LiveClientData
from ..core import Quest, TaskEvaluator, RestrictionEffect
from ..content.evaluators import StatTaskEvaluator


class QuestManager:
    def __init__(self):
        self.active_quests = []
        self.live_client_data_fetcher = LiveClientDataFetcher()

    def loop(self):
        # test
        evaluator = StatTaskEvaluator(
            "get_ability_power",
            "Get ability power.",
            ["stat", "ability_power"],
            300,
            20,
            stat_type="ability_power",
            target_value=20,
        )
        restriction = RestrictionEffect(
            "No Attack", "You cannot use basic attacks.", ["attack"]
        )
        quest = Quest(evaluator, restriction)

        last_time = None
        while True:
            data = self.live_client_data_fetcher.fetch()
            if data is None:
                continue

            live_client_data = LiveClientData(data)

            t = live_client_data.get_game_time()
            if t is None:
                continue

            if last_time is None:
                last_time = t
                quest.start(live_client_data)

            dt = t - last_time
            last_time = t

            quest.update(dt, live_client_data)

            # print completed, failed, holding, time left, holding timer, stat value each on a new line
            print("-----")
            print(f"Completed: {quest.is_completed()}")
            print(f"Failed: {quest.is_failed()}")
            print(f"Time Left: {quest.get_time_left()}")
            print(f"Holding: {quest.is_holding()}")
            print(f"Completion Timer: {quest.get_completion_time_left()}")
            print(f"Current Value: {quest.get_progress()}")
            print(f"Goal: {quest.get_goal()}")

            time.sleep(1)
