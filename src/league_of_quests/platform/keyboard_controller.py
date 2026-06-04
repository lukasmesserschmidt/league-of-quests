import time
import threading
import keyboard

from .live_client import LiveClient


class KeyboardController:
    def __init__(self):
        # Key-level reference counting: key -> number of owners requesting block
        self._key_ref_counts: dict[str, int] = {}
        # Track which keys are currently physically blocked by the keyboard library
        self._physically_blocked: set[str] = set()
        self._lock = threading.Lock()
        self._live_client = LiveClient()

        self._monitor_thread = threading.Thread(target=self._focus_monitor, daemon=True)
        self._monitor_thread.start()

    def block_key(self, key: str):
        """Request to block a key. Key is only blocked if live client is focused."""
        with self._lock:
            if key not in self._key_ref_counts:
                self._key_ref_counts[key] = 0
            self._key_ref_counts[key] += 1

            if self._live_client.is_focused():
                self._physically_block_key(key)

    def unblock_key(self, key: str):
        """Release a block request. Key is unblocked only when no owners want it blocked."""
        with self._lock:
            if key not in self._key_ref_counts:
                return

            self._key_ref_counts[key] -= 1

            if self._key_ref_counts[key] <= 0:
                del self._key_ref_counts[key]
                self._physically_unblock_key(key)

    def _focus_monitor(self):
        """Monitor focus state and block/unblock keys accordingly."""
        was_focused = False
        while True:
            is_focused = self._live_client.is_focused()
            if is_focused != was_focused:
                with self._lock:
                    if is_focused:
                        # Block all keys that have ref count > 0
                        for key in self._key_ref_counts.keys():
                            self._physically_block_key(key)
                    else:
                        # Unblock all physically blocked keys
                        for key in list(self._physically_blocked):
                            self._physically_unblock_key(key)
                was_focused = is_focused
            time.sleep(0.1)

    def _physically_block_key(self, key: str):
        """Actually block the key using the keyboard library."""
        if key in self._physically_blocked:
            return

        self._physically_blocked.add(key)
        keyboard.block_key(key)

    def _physically_unblock_key(self, key: str):
        """Actually unblock the key using the keyboard library."""
        if key not in self._physically_blocked:
            return

        self._physically_blocked.remove(key)
        keyboard.unblock_key(key)
