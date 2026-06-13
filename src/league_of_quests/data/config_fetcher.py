import json

from .models import Config, DEFAULT_CONFIG
from .resources import get_config_path
from ..utils import SingletonMeta


class ConfigFetcher(metaclass=SingletonMeta):
    def __init__(self):
        self._config = None
        self._config_path = get_config_path()
        self._last_modified = 0

    def fetch(self):
        try:
            modified = self._config_path.stat().st_mtime

            if self._config is None or self._last_modified != modified:
                self._config = self._load_config()
                self._last_modified = modified
        except Exception:
            self._config = Config(**DEFAULT_CONFIG)

        return self._config

    def _load_config(self):
        if not self._config_path.exists():
            self._write_default_config()

        try:
            with open(self._config_path, "r", encoding="utf-8") as f:
                config = json.load(f)

            return Config(**config)
        except Exception:
            return Config(**DEFAULT_CONFIG)

    def _write_default_config(self):
        try:
            with open(self._config_path, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
        except Exception:
            pass
