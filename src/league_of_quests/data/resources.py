import json
from pathlib import Path


def get_lol_config_path():
    # 1. Determine the path to the RiotClientInstalls.json depending on the OS
    riot_installs_json = Path("C:\\ProgramData\\Riot Games\\RiotClientInstalls.json")

    if not riot_installs_json.exists():
        raise FileNotFoundError(f"Riot Client configuration not found at: {riot_installs_json}")

    # 2. Parse the JSON file and extract the path
    with open(riot_installs_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Search for the League of Legends install path in the "associated_client" section
    for client_path in data.get("associated_client", {}).keys():
        if client_path.endswith("/Riot Games/League of Legends/"):
            lol_path_str = client_path
            break
    else:
        raise FileNotFoundError(
            "League of Legends installation path was not found in the Riot configuration."
        )

    # 3. Verify the path to the config file
    lol_base_path = Path(lol_path_str)
    lol_config_path = lol_base_path / "Config"

    if not lol_config_path.exists():
        raise FileNotFoundError(
            f"The Config folder does not exist at the specified location: {lol_config_path}"
        )

    return lol_config_path


def get_inputini_path():
    lol_config_path = get_lol_config_path()
    return lol_config_path / "input.ini"


def get_gamecfg_path():
    lol_config_path = get_lol_config_path()
    return lol_config_path / "game.cfg"


def get_config_path():
    return Path(__file__).parent.parent.parent.parent / "config" / "config.json"
