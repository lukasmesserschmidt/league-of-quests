from .live_client_data import request_data


class AllPlayerDate:
    @classmethod
    def get_data(cls):
        url = "​https://127.0.0.1:2999/liveclientdata/playerlist"
        return request_data(url)

    @classmethod
    def get_team_players(cls, team):
        pass
