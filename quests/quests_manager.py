from random import randint
import threading
import time

from . import quests as qu
from ..lol_data.live_game_data import LolData


class QuestManager:
    all_quests = [
        qu.Test,
    ]

    available_quests: list

    active_quests: list

    sync_time = 60
    remaining_sync_time = 0
    time_til_quest = 0
    easy_chance = 70
    mid_chance = 20
    hard_chance = 10

    @classmethod
    def update_available_quests(cls):
        cls.available_quests = [[], [], []]

        for quest in cls.all_quests:
            if quest not in cls.active_quests and quest.check_dependencies:
                cls.available_quests[quest.difficulty].append(quest)

    @classmethod
    def get_difficulty(cls):
        all_chances = cls.easy_chance + cls.mid_chance + cls.hard_chance
        roll = randint(1, all_chances)

        if len(cls.available_quests[2]) > 0 and roll <= cls.hard_chance:
            return 2
        elif (
            len(cls.available_quests[1]) > 0
            and roll <= cls.mid_chance + cls.hard_chance
        ):
            return 1
        elif len(cls.available_quests[0]) > 0:
            return 0

        return None

    @classmethod
    def start(cls):
        start_time = time.time() + cls.sync_time
        while time.time() > start_time:
            cls.remaining_sync_time = start_time - time.time()

        activate_quests = threading.Thread(target=cls.activate_quests, daemon=True)
        activate_quests.start()

    @classmethod
    def activate_quests(cls):
        while True:
            cls.update_available_quests()
            difficulty = cls.get_difficulty()

            if difficulty != None:
                rand_quest_idx = randint(0, len(cls.available_quests[difficulty]) - 1)
                quest = cls.available_quests[difficulty][rand_quest_idx]
                quest.start()
                cls.active_quests.append(quest)

            time.sleep(60)
