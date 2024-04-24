from .live_client_data import LiveClientData
from .event_data import EventData
from .all_player_data import AllPlayerDate


class AcitvePlayerData:
    @classmethod
    def get_data(cls):
        return LiveClientData.request_data()["activePlayer"]

    @classmethod
    def get_summoner_name(cls):
        return cls.get_data()["summonerName"].split("#")[0]

    @classmethod
    def get_champion_stats(cls):
        return cls.get_data()["championStats"]

    @classmethod
    def get_level(cls):
        return cls.get_data()["level"]

    @classmethod
    def get_ability_level(cls):
        abilities = cls.get_data()["abilities"]
        ability_level = {
            "q": abilities["Q"]["abilityLevel"],
            "w": abilities["W"]["abilityLevel"],
            "e": abilities["E"]["abilityLevel"],
            "r": abilities["R"]["abilityLevel"],
        }

        return ability_level

    @classmethod
    def get_team(cls):
        teams = AllPlayerDate.get_team_players()
        summoner_name = cls.get_summoner_name()

        for num, team in enumerate(teams):
            for player in team:
                if player["summonerName"] == summoner_name:
                    return num

    @classmethod
    def get_current_gold(cls):
        return cls.get_data()["currentGold"]

    @classmethod
    def get_health_data(cls):
        champion_stats = cls.get_champion_stats()
        health_data = {
            "max": champion_stats["maxHealth"],
            "value": champion_stats["currentHealth"],
        }

        return health_data

    @classmethod
    def get_resource_data(cls):
        champion_stats = cls.get_champion_stats()
        resource_data = {
            "type": champion_stats["resourceType"],
            "max": champion_stats["resourceMax"],
            "value": champion_stats["resourceValue"],
        }

        return resource_data

    @classmethod
    def get_death_count(cls):
        events = EventData.get_kill_events()
        death_count = 0

        for event in events:
            if event["VictimName"] == cls.get_summoner_name():
                death_count += 1

        return death_count
