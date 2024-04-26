from .quest_completion_base import QuestCompletionBase
from ..lol_data.active_player_data import AcitvePlayerData
from ..lol_data.score_data import ScoreData
from ..lol_data.item_data import ItemData
from ..utils.attributes import BUY


class BuyDarkSeal(QuestCompletionBase):
    title = "Buy a Dark Seal XD!"
    difficulty = 2
    attributes = [BUY]

    @classmethod
    def check_dependencies(cls):
        summoner_name = AcitvePlayerData.get_summoner_name()
        if ItemData.get_has_item(summoner_name, 1082) == None:
            kda_data = ScoreData.get_k_d_a(summoner_name)
            kda = (kda_data["k"] + kda_data["a"]) / (kda_data["d"] or 1)

            if kda_data["d"] > 3 and kda <= 0.8:
                return True

    @classmethod
    def init(cls):
        super().init()
        cls.summoner_name = AcitvePlayerData.get_summoner_name()

    @classmethod
    def quest_content(cls):
        cls.set_complete(ItemData.get_has_item(cls.summoner_name, 1082))
