import time

from .quest_base import QuestBase
from ..lol_data.active_player_data import AcitvePlayerData
from ..manager.settings_manager import Settings
from ..utils.constants import GOLD


class SpendGoldTimer(QuestBase):
    title = "Spend gold or timer x2"
    difficulty = 1
    attributes = [GOLD]

    @classmethod
    def quest_loop(cls):
        cls.on_quest_start()
        gold_spend = False
        duration = Settings.all_settings["quest_settings"]["quest_duration"] / 12

        for _ in range(4):
            end_time = time.time() + duration

            while time.time() < end_time:
                cls.remaining_time = end_time - time.time()
                if cls.quest_content():
                    gold_spend = True
                    cls.finish_color_enabled = True

            if cls.terminate_flag or gold_spend:
                break

            duration *= 2

        cls.terminate_flag = True

    @classmethod
    def on_quest_start(cls):
        cls.last_gold = AcitvePlayerData.get_current_gold()

    @classmethod
    def quest_content(cls):
        current_gold = AcitvePlayerData.get_current_gold()

        if current_gold < cls.last_gold:
            return True

        cls.last_gold = current_gold
