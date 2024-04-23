from .get_live_client_data import request_data


class ItemData:

    @classmethod
    def get_data(cls, summoner_name: str):
        url = (
            "https://127.0.0.1:2999/liveclientdata/playeritems?summonerName="
            + summoner_name
        )
        return request_data(url)

    @classmethod
    def get_has_item(cls, summoner_name, item_id):
        items = cls.get_data(summoner_name)

        for item in items:
            if item["itemID"] == item_id:
                return True
