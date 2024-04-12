import json


class GetLolSettings:
    riot_client_installs_path = "C:/ProgramData/Riot Games/RiotClientInstalls.json"

    @classmethod
    def get_lol_settings_path(cls):
        with open(cls.riot_client_installs_path, "r") as f:
            riot_client_path = json.load(f)["associated_client"][
                "C:/Riot Games/League of Legends/"
            ]

        riot_games_path = riot_client_path[
            0 : -len("/Riot Client/RiotClientServices.exe")
        ]

        cls.lol_settings_path = (
            riot_games_path + "/League of Legends/Config/PersistedSettings.json"
        )

    @classmethod
    def import_lol_settings(cls):
        with open(cls.lol_settings_path, "r") as f:
            cls.all_lol_settings = json.load(f)
