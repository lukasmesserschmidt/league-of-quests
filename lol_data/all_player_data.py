from .get_live_client_data import request_data


class AllPlayerDate:
    @classmethod
    def get_data(cls):
        url = "https://127.0.0.1:2999/liveclientdata/playerlist"
        return request_data(url)

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
