from .get_live_client_data import request_data


class ScoreData:
    @classmethod
    def get_data(cls, summoner_name: str):
        url = (
            "https://127.0.0.1:2999/liveclientdata/playerscores?summonerName="
            + summoner_name
        )
        return request_data(url)

    @classmethod
    def get_cs(cls, summoner_name):
        return cls.get_data(summoner_name)["creepScore"]

    @classmethod
    def get_k_d_a(cls, summoner_name):
        scores = cls.get_data(summoner_name)
        kda = {"k": scores["kills"], "d": scores["deaths"], "a": scores["assists"]}

        return kda
