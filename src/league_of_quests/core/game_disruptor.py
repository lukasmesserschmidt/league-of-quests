import threading
import time
from typing import Optional

from ..platform.keyboard_controller import KeyboardController
from ..data.live_client_config_monitor import LiveClientConfigMonitor
from .enums import HotkeyType


class GameDisruptor:
    def __init__(self):
        self._keyboard_controller = KeyboardController()
        self._config_monitor = LiveClientConfigMonitor()
        self._lock = threading.Lock()

        # Reference counting for blocked abilities: HotkeyType -> count
        self._blocked_abilities: dict[HotkeyType, int] = {}

        # Track current hotkeys for each ability: HotkeyType -> key string
        self._current_hotkeys: dict[HotkeyType, list[str]] = {}

        # Start monitoring hotkey changes
        self._monitor_thread = threading.Thread(target=self._hotkey_monitor, daemon=True)
        self._monitor_thread.start()

    def disable_ability(self, ability: HotkeyType):
        with self._lock:
            # Increment reference count
            self._blocked_abilities[ability] = self._blocked_abilities.get(ability, 0) + 1

            # Get current hotkey and block it
            hotkey = self._get_hotkey_for_ability(ability)
            if hotkey:
                self._current_hotkeys[ability] = hotkey
                for key in hotkey:
                    self._keyboard_controller.block_key(key)

    def enable_ability(self, ability: HotkeyType):
        with self._lock:
            if ability not in self._blocked_abilities:
                return

            # Decrement reference count
            self._blocked_abilities[ability] -= 1

            # If count reaches zero, unblock the key
            if self._blocked_abilities[ability] <= 0:
                del self._blocked_abilities[ability]

                # Unblock the current hotkey
                hotkey = self._current_hotkeys.get(ability)
                if hotkey:
                    for key in hotkey:
                        self._keyboard_controller.unblock_key(key)
                    del self._current_hotkeys[ability]

    def is_ability_disabled(self, ability: HotkeyType) -> bool:
        with self._lock:
            return ability in self._blocked_abilities

    def _get_hotkey_for_ability(self, ability: HotkeyType) -> Optional[list[str]]:
        config = self._config_monitor.get_config()
        if not config:
            return None

        return getattr(config.input, ability.value, None)

    def _hotkey_monitor(self):
        while True:
            try:
                with self._lock:
                    for ability in self._blocked_abilities.keys():
                        new_hotkey = self._get_hotkey_for_ability(ability)
                        old_hotkey = self._current_hotkeys.get(ability)

                        if new_hotkey and new_hotkey != old_hotkey:
                            # Unblock old hotkey
                            if old_hotkey:
                                for key in old_hotkey:
                                    self._keyboard_controller.unblock_key(key)

                            # Block new hotkey
                            for key in new_hotkey:
                                self._keyboard_controller.block_key(key)
                            self._current_hotkeys[ability] = new_hotkey
            except Exception:
                pass

            time.sleep(0.5)
