from random import randint, choice

from .quest_completion_base import QuestCompletionBase
from ..lol_data.active_player_data import ActivePlayerData
from ..lol_data.item_data import ItemData
from ..utils.constants import Constants


class GetXStat(QuestCompletionBase):
    title = "Get x name!"
    difficulty = 0
    attributes = [Constants.BUY]

    update_title = True

    @classmethod
    def check_dependencies(cls):
        return len(ItemData.get_data(ActivePlayerData.get_summoner_name())) < 7

    @classmethod
    def init(cls):
        super().init()
        stats = {
            "maxHealth": [110, 170],
            "attackDamage": [5, 13],
            "abilityPower": [10, 25],
            "armor": [5, 20],
            "magicResist": [15, 30],
            "abilityHaste": [3, 6],
            "critChance": [15, 15],
        }

        cls.stat_name, stat_limits = choice(list(stats.items()))
        cls.stat_goal = randint(stat_limits[0], stat_limits[1])
        cls.start_value = cls.get_current_value()

        cls.set_title(0)

    @classmethod
    def quest_content(cls):
        current_value = cls.get_current_value()
        progress = current_value - cls.start_value

        cls.set_title(progress)

        cls.complete = progress >= cls.stat_goal

    @classmethod
    def get_current_value(cls):
        return ActivePlayerData.get_champion_stat(cls.stat_name) * (
            100 if cls.stat_name == "critChance" else 1
        )

    @classmethod
    def set_title(cls, progress: float):
        cls.title = f"Get {int(progress)}/{cls.stat_goal} {cls.stat_name.upper()}!"
