from .all_player_data import AllPlayerData


class ScoreData:
    @classmethod
    def get_data(cls, summoner_name: str):
        return AllPlayerData.get_player_data(summoner_name)["scores"]

    @classmethod
    def get_cs(cls, summoner_name: str):
        return cls.get_data(summoner_name)["creepScore"]

    @classmethod
    def get_k_d_a(cls, summoner_name: str):
        scores = cls.get_data(summoner_name)
        kda = {"k": scores["kills"], "d": scores["deaths"], "a": scores["assists"]}

        return kda

    @classmethod
    def get_ward_score(cls, summoner_name: str):
        return cls.get_data(summoner_name)["wardScore"]
