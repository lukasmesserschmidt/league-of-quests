from .all_player_data import AllPlayerData


class ScoreData:
    @classmethod
    def get_data(cls, summoner_name: str):
        return AllPlayerData.get_player_data(summoner_name)["scores"]

    @classmethod
    def get_cs(cls, summoner_name: str):
        return cls.get_data(summoner_name)["creepScore"]

    @classmethod
    def get_kills(cls, summoner_name: str):
        scores = cls.get_data(summoner_name)
        kills = scores["kills"]

        return kills

    @classmethod
    def get_deaths(cls, summoner_name: str):
        scores = cls.get_data(summoner_name)
        kills = scores["deaths"]

        return kills

    @classmethod
    def get_assists(cls, summoner_name: str):
        scores = cls.get_data(summoner_name)
        kills = scores["assists"]

        return kills

    @classmethod
    def get_ward_score(cls, summoner_name: str):
        return cls.get_data(summoner_name)["wardScore"]
