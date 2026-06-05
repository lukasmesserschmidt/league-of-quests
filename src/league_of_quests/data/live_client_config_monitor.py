import configparser

from .live_client_config import Game, Input, LiveClientConfig
from .resources import get_gamecfg_path, get_inputini_path
from ..utils import parse_hotkey


class LiveClientConfigMonitor:
    def __init__(self):
        self._config = None
        self._input_ini_path = get_inputini_path()
        self._game_cfg_path = get_gamecfg_path()
        self._last_modified_input = 0
        self._last_modified_game = 0

        # Initial load
        self._update_config()

    def get_config(self):
        # Check if files have been modified
        try:
            input_modified = self._input_ini_path.stat().st_mtime
            game_modified = self._game_cfg_path.stat().st_mtime

            if (
                input_modified != self._last_modified_input
                or game_modified != self._last_modified_game
            ):
                self._last_modified_input = input_modified
                self._last_modified_game = game_modified
                self._update_config()
        except (FileNotFoundError, OSError):
            pass

        return self._config

    def _update_config(self):
        try:
            # Parse input.ini
            input_config = configparser.ConfigParser()
            input_config.read(self._input_ini_path)

            # Parse game.cfg
            game_config = configparser.ConfigParser()
            game_config.read(self._game_cfg_path)

            # Extract only the fields defined in live_client_config.py
            # Let pydantic handle type conversion and validation with defaults
            input_data = Input(
                evtCastSpell4=parse_hotkey(input_config.get("GameEvents", "evtCastSpell4")),
                evtCastSpell3=parse_hotkey(input_config.get("GameEvents", "evtCastSpell3")),
                evtCastSpell2=parse_hotkey(input_config.get("GameEvents", "evtCastSpell2")),
                evtCastSpell1=parse_hotkey(input_config.get("GameEvents", "evtCastSpell1")),
            )

            game_data = Game(
                MinimapScale=game_config.get("HUD", "MinimapScale"),
                GlobalScale=game_config.get("HUD", "GlobalScale"),
                FlipMiniMap=game_config.get("HUD", "FlipMiniMap"),
                Width=game_config.get("General", "Width"),
                Height=game_config.get("General", "Height"),
            )

            self._config = LiveClientConfig(game=game_data, input=input_data)
        except (configparser.Error, FileNotFoundError, OSError):
            pass
