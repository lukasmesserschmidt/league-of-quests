from .quest_completion_base import QuestCompletionBase
from ..lol_data.active_player_data import ActivePlayerData
from ..lol_data.item_data import ItemData
from ..utils.attributes import BUY


class BuyDarkSeal(QuestCompletionBase):
    title = "Buy a Dark Seal XD!"
    difficulty = 2
    attributes = [BUY]

    @classmethod
    def check_dependencies(cls):
        summoner_name = ActivePlayerData.get_summoner_name()
        if ItemData.get_has_item(summoner_name, 1082) == None:
            kills = ActivePlayerData.get_kills()
            deaths = ActivePlayerData.get_deaths()
            assists = ActivePlayerData.get_assists()
            kda = (kills + assists) / (deaths or 1)

            if deaths > 3 and kda <= 0.8:
                return True

    @classmethod
    def init(cls):
        super().init()
        cls.summoner_name = ActivePlayerData.get_summoner_name()

    @classmethod
    def quest_content(cls):
        cls.complete = bool(ItemData.get_has_item(cls.summoner_name, 1082))
