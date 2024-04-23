import json


def get_riot_games_path():
    riot_client_installs_path = "C:/ProgramData/Riot Games/RiotClientInstalls.json"

    with open(riot_client_installs_path, "r") as f:
        riot_client_path = json.load(f)["associated_client"][
            "C:/Riot Games/League of Legends/"
        ]

    riot_games_path = riot_client_path[0 : -len("/Riot Client/RiotClientServices.exe")]

    return riot_games_path


def get_lol_config_path():
    riot_games_path = get_riot_games_path()

    lol_config_path = riot_games_path + "/League of Legends/Config"

    return lol_config_path


def get_lol_settings_path():
    lol_config_path = get_lol_config_path()

    lol_settings_path = lol_config_path + "/PersistedSettings.json"

    return lol_settings_path
