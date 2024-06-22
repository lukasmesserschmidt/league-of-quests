"""
This module contains functions to get the League of Legends paths.
"""

import json


def get_lol_config_path():
    """
    Returns the Config folder path.
    """
    riot_client_installs_path = "C:/ProgramData/Riot Games/RiotClientInstalls.json"

    with open(riot_client_installs_path, "r", encoding="utf-8") as f:
        associated_clients: dict
        associated_clients = json.load(f)["associated_client"]

    for path in associated_clients.keys():
        if "/Riot Games/League of Legends/" in path:
            return path + "Config"


def get_lol_settings_path():
    """
    Returns the PersistedSettings.json path.
    """
    lol_config_path = get_lol_config_path()

    lol_settings_path = lol_config_path + "/PersistedSettings.json"

    return lol_settings_path


def get_game_cfg_path():
    """
    Returns the game.cfg path.
    """
    lol_config_path = get_lol_config_path()

    game_cfg_path = lol_config_path + "/game.cfg"

    return game_cfg_path
