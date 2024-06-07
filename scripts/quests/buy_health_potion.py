from random import randint

from .quest_completion_base import QuestCompletionBase
from ..lol_data.active_player_data import ActivePlayerData
from ..lol_data.item_data import ItemData
from ..utils.constants import Constants


class BuyHealthPotion(QuestCompletionBase):
    title = "Buy ? health potions!"
    difficulty = None
    attributes = [Constants.BUY]

    update_title = True

    alternating_difficulties = (0, 1)

    @classmethod
    def check_dependencies(cls):
        summoner_name = ActivePlayerData.get_summoner_name()
        return len(ItemData.get_data(summoner_name)) < 7 and not ItemData.get_has_item(
            summoner_name, 2003
        )

    @classmethod
    def init(cls):
        super().init()
        cls.summoner_name = ActivePlayerData.get_summoner_name()
        cls.potion_amount = 2 * (cls.difficulty + 1)

        cls.set_title(0)

    @classmethod
    def quest_content(cls):
        potion_count = ItemData.get_item_count(cls.summoner_name, 2003)

        cls.set_title(potion_count)

        cls.complete = potion_count >= cls.potion_amount

    @classmethod
    def set_title(cls, progress: float):
        cls.title = f"Buy {progress}/{cls.potion_amount} health potions!"
