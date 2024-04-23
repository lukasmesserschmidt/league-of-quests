import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .get_lol_paths import get_lol_config_path, get_lol_settings_path


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("PersistedSettings.json"):
            GetLolSettings.import_settings()


class GetLolSettings:
    all_lol_settings = {}

    @classmethod
    def import_settings(cls):
        imported = False
        while imported == False:
            try:
                with open(get_lol_settings_path(), "r") as f:
                    cls.all_lol_settings = json.load(f)
                    imported = True
            except:
                pass

    @classmethod
    def start(cls):
        cls.import_settings()
        path = get_lol_config_path()
        cls.event_handler = MyHandler()
        cls.observer = Observer()
        cls.observer.schedule(cls.event_handler, path, recursive=False)
        cls.observer.start()

    @classmethod
    def stop(cls):
        cls.observer.stop()
        cls.observer.join()
