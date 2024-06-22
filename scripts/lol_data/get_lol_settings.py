"""
This module contains the GetLolSettings class.
"""

import time

from contextlib import suppress
import configparser
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .get_lol_paths import get_lol_config_path, get_lol_settings_path, get_game_cfg_path


class Handler(FileSystemEventHandler):
    """
    Observes the changes in the PersistedSettings.json and game.cfg files.
    """

    def on_modified(self, event):
        if event.src_path.endswith("PersistedSettings.json") or event.src_path.endswith(
            "game.cfg"
        ):
            time.sleep(0.1)
            GetLolSettings.import_settings()
            GetLolSettings.import_game_cfg()


class GetLolSettings:
    """
    This class gets the League of Legends settings.
    """

    # init variables
    all_lol_settings: dict
    game_cfg: configparser.ConfigParser
    all_lol_settings = None
    game_cfg = None

    observer = None

    @classmethod
    def import_settings(cls):
        """
        Imports the persisted settings.
        """
        imported = False

        while not imported:
            with suppress(Exception):
                with open(get_lol_settings_path(), "r", encoding="utf-8") as f:
                    cls.all_lol_settings = json.load(f)
                    imported = True

    @classmethod
    def import_game_cfg(cls):
        """
        Imports the game.cfg.
        """
        imported = False

        while not imported:
            game_cfg_path = get_game_cfg_path()
            game_cfg = configparser.ConfigParser()
            game_cfg.read(game_cfg_path)

            with suppress(Exception):
                _ = game_cfg.get("General", "Width")
                cls.game_cfg = game_cfg
                imported = True

    @classmethod
    def start(cls):
        """
        Starts the import loop and imports the settings and game.cfg once.
        """
        if cls.observer is None:
            cls.import_settings()
            cls.import_game_cfg()
            path = get_lol_config_path()
            event_handler = Handler()
            cls.observer = Observer()
            cls.observer.schedule(event_handler, path, recursive=False)

            cls.observer.start()

    @classmethod
    def stop(cls):
        """
        Stops the import loop.
        """
        if cls.observer is not None:
            cls.observer.stop()
            cls.observer.join()
