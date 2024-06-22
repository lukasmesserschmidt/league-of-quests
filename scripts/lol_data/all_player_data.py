"""
This module contains the AllPlayerData class.
"""

from .get_live_client_data import GetLiveClientData


class AllPlayerData:
    """
    This class contains the data of all players.
    """

    @classmethod
    def get_data(cls):
        return GetLiveClientData.all_data["allPlayers"]

    @classmethod
    def get_player_data(cls, summoner_name: str):
        all_players = cls.get_data()

        for player in all_players:
            if player["riotIdGameName"] == summoner_name:
                return player

    @classmethod
    def get_team_players(cls):
        all_players = cls.get_data()
        teams = [[], []]

        for player in all_players:
            if player["team"] == "ORDER":
                teams[0].append(player)
            else:
                teams[1].append(player)

        return teams
