from contextlib import suppress
import configparser
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .get_lol_paths import get_lol_config_path, get_lol_settings_path, get_game_cfg_path


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("PersistedSettings.json") or event.src_path.endswith(
            "game.cfg"
        ):
            GetLolSettings.import_settings()
            GetLolSettings.import_game_cfg()


class GetLolSettings:
    all_lol_settings: dict
    all_lol_settings = None
    game_cfg: configparser.ConfigParser
    game_cfg = None

    observer = None

    @classmethod
    def import_settings(cls):
        with suppress(Exception):
            with open(get_lol_settings_path(), "r") as f:
                cls.all_lol_settings = json.load(f)

    @classmethod
    def import_game_cfg(cls):
        game_cfg_path = get_game_cfg_path()
        game_cfg = configparser.ConfigParser()
        game_cfg.read(game_cfg_path)

        with suppress(Exception):
            _ = game_cfg.get("General", "Width")
            cls.game_cfg = game_cfg

    @classmethod
    def start(cls):
        if cls.observer is None:
            cls.import_settings()
            cls.import_game_cfg()
            path = get_lol_config_path()
            event_handler = MyHandler()
            cls.observer = Observer()
            cls.observer.schedule(event_handler, path, recursive=False)

        cls.observer.start()

    @classmethod
    def stop(cls):
        if cls.observer is not None:
            cls.observer.stop()
            cls.observer.join()
