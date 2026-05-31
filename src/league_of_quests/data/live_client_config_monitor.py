import configparser
import os
import time
from threading import Thread, Lock

from .live_client_config import Game, Input, LiveClientConfig
from .resources import get_gamecfg_path, get_inputini_path
from ..utils import parse_hotkey


class LiveClientConfigMonitor:
    def __init__(self):
        self._config = None
        self._lock = Lock()
        self._input_ini_path = get_inputini_path()
        self._game_cfg_path = get_gamecfg_path()
        self._last_modified_input = 0
        self._last_modified_game = 0
        self._running = False
        self._thread = None

        # Initial load
        self._update_config()

        # Start monitoring
        self._start_monitoring()

    def get_config(self):
        with self._lock:
            return self._config

    def _start_monitoring(self):
        self._running = True
        self._thread = Thread(target=self._monitor_thread, daemon=True)
        self._thread.start()

    def _stop_monitoring(self):
        self._running = False
        if self._thread:
            self._thread.join()

    def _monitor_thread(self):
        while self._running:
            try:
                input_modified = os.path.getmtime(self._input_ini_path)
                game_modified = os.path.getmtime(self._game_cfg_path)

                if (
                    input_modified != self._last_modified_input
                    or game_modified != self._last_modified_game
                ):
                    self._last_modified_input = input_modified
                    self._last_modified_game = game_modified
                    self._update_config()
            except (FileNotFoundError, OSError):
                pass

            time.sleep(0.5)

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

            game_data = Game(MinimapScale=game_config.get("HUD", "MinimapScale"))

            with self._lock:
                self._config = LiveClientConfig(game=game_data, input=input_data)
        except (configparser.Error, FileNotFoundError, OSError):
            pass
