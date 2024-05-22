from .get_live_client_data import GetLiveClientData
from .event_data import EventData
from .score_data import ScoreData
from .all_player_data import AllPlayerData


class ActivePlayerData:
    @classmethod
    def get_data(cls) -> dict:
        return GetLiveClientData.all_data["activePlayer"]

    @classmethod
    def get_summoner_name(cls):
        return cls.get_data()["riotIdGameName"]

    @classmethod
    def get_champion_name(cls):
        summoner_name = cls.get_summoner_name()
        return AllPlayerData.get_player_data(summoner_name)["championName"]

    @classmethod
    def get_champion_stat(cls, name: str):
        return cls.get_data()["championStats"][name]

    @classmethod
    def get_level(cls):
        return cls.get_data()["level"]

    @classmethod
    def get_ability_level(cls, ability: str):
        return cls.get_data()["abilities"][ability]["abilityLevel"]

    @classmethod
    def get_team_num(cls):
        teams = AllPlayerData.get_team_players()
        summoner_name = cls.get_summoner_name()

        for num, team in enumerate(teams):
            for player in team:
                if player["riotIdGameName"] == summoner_name:
                    return num

    @classmethod
    def get_teammates(cls):
        summoner_name = cls.get_summoner_name()
        ally_team_num = cls.get_team_num()
        teammates: list
        teammates = AllPlayerData.get_team_players()[ally_team_num]
        for player in teammates:
            if player["riotIdGameName"] == summoner_name:
                teammates.remove(player)
                break

        return teammates

    @classmethod
    def get_enemy_team(cls):
        ally_team_num = cls.get_team_num()
        all_teams = AllPlayerData.get_team_players()
        enemy_team = all_teams[ally_team_num - 1]

        return enemy_team

    @classmethod
    def get_current_gold(cls):
        return cls.get_data()["currentGold"]

    @classmethod
    def get_kills(cls):
        return ScoreData.get_kills(cls.get_summoner_name())

    @classmethod
    def get_deaths(cls):
        return ScoreData.get_deaths(cls.get_summoner_name())

    @classmethod
    def get_assists(cls):
        return ScoreData.get_assists(cls.get_summoner_name())
