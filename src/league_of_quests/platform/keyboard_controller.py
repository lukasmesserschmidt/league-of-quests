import time
import threading
import keyboard

from .live_client import LiveClient


class KeyboardController:
    def __init__(self):
        self._blocked_keys = set()
        self._lock = threading.Lock()
        self._live_client = LiveClient()

        self._monitor_thread = threading.Thread(target=self._focus_monitor, daemon=True)
        self._monitor_thread.start()

    def block_key(self, key: str):
        with self._lock:
            self._blocked_keys.add(key)

            if self._live_client.is_focused():
                keyboard.block_key(key)

    def unblock_key(self, key: str):
        with self._lock:
            if key in self._blocked_keys:
                self._blocked_keys.remove(key)
                try:
                    keyboard.unblock_key(key)
                except KeyError:
                    pass

    def press_release_key(self, key: str):
        if self._live_client.is_focused():
            keyboard.press_and_release(key)

    def _focus_monitor(self):
        was_focused = False
        while True:
            is_focused = self._live_client.is_focused()
            if is_focused != was_focused:
                with self._lock:
                    for key in self._blocked_keys:
                        if is_focused:
                            keyboard.block_key(key)
                        else:
                            keyboard.unblock_key(key)
                was_focused = is_focused
            time.sleep(0.1)
