from .all_player_data import AllPlayerDate


class ItemData:

    @classmethod
    def get_data(cls, summoner_name: str):
        return AllPlayerDate.get_player_data(summoner_name)["items"]

    @classmethod
    def get_has_item(cls, summoner_name: str, item_id: int):
        items = cls.get_data(summoner_name)

        for item in items:
            if item["itemID"] == item_id:
                return True
