from .all_player_data import AllPlayerData


class ItemData:

    @classmethod
    def get_data(cls, summoner_name: str):
        return AllPlayerData.get_player_data(summoner_name)["items"]

    @classmethod
    def get_has_item(cls, summoner_name: str, item_id: int):
        items = cls.get_data(summoner_name)

        for item in items:
            if item["itemID"] == item_id:
                return True

        return False

    @classmethod
    def get_item_count(cls, summoner_name: str, item_id: int):
        items = cls.get_data(summoner_name)

        for item in items:
            if item["itemID"] == item_id:
                return item["count"]

        return 0
