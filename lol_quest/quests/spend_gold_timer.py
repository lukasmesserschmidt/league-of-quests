from .quest_base import QuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.attributes import GOLD


class SpendGoldTimer(QuestBase):
    title = "Spend gold or timer x2!"
    difficulty = 1
    attributes = [GOLD]

    @classmethod
    def init(cls):
        cls.duration = cls.get_duration(1 / 12)
        cls.gold_spend = False
        cls.last_gold = ActivePlayerData.get_current_gold()

    @classmethod
    def quest_loop_container(cls):
        for _ in range(4):
            cls._quest_loop()

            cls.duration *= 2

            if cls.gold_spend:
                break

    @classmethod
    def quest_content(cls):
        current_gold = ActivePlayerData.get_current_gold()

        if current_gold < cls.last_gold:
            cls.gold_spend = True
            cls.finish_color_enabled = True

        cls.last_gold = current_gold
