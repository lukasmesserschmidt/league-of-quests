import tkinter as tk
import threading
import time

from ..lol_data.live_game_data import LolData
from .. import settings_manager


###base quest classes###
class QuestBase:
    unlocked = True
    name: str
    description: str
    difficulty: int
    quest_duration: int
    completion_duration = 0
    dependencies = ()
    incompatible = ()

    remaining_quest_time = 0
    remaining_completion_time = 0

    @classmethod
    def init(cls):
        my_quest_settings = settings_manager.all_settings["quests"][cls.name]
        cls.unlocked = my_quest_settings["unlocked"]
        cls.quest_duration = my_quest_settings["qduration"]
        cls.completion_duration = my_quest_settings["cduration"]

    @classmethod
    def start(cls):
        quest = threading.Thread(target=cls.run_quest)
        quest.start()

    @classmethod
    def run_quest(cls):
        cls.on_quest_start()
        end_time = time.time() + cls.quest_duration
        while time.time() < end_time:
            cls.remaining_time = end_time - time.time()
            if cls.quest_content():
                break

    @classmethod
    def on_quest_start(cls):
        pass

    @classmethod
    def quest_content(cls):
        raise NotImplementedError()


###quest classes###
class Test(QuestBase):
    name = "test"
    difficulty = 0
    duration = 10

    @classmethod
    def on_quest_start(cls):
        cls.last_gold = LolData.get_activePlayer_data("currentGold")

    @classmethod
    def quest_content(cls):
        current_gold = LolData.get_activePlayer_data("currentGold")
        if current_gold < cls.last_gold:
            print("fail")
            return True

        cls.last_gold = current_gold


# LolData.init()
# Test.start()
