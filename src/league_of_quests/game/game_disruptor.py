import threading
import time
from typing import Optional

from .game_overlay import GameOverlay
from ..platform.keyboard_controller import KeyboardController
from ..data import LiveClientConfigFetcher, HotkeyType


class GameDisruptor:
    def __init__(self, game_overlay: GameOverlay):
        self._keyboard_controller = KeyboardController()
        self._live_client_config_fetcher = LiveClientConfigFetcher()
        self._lock = threading.Lock()

        self._game_overlay = game_overlay

        # Track owners of blocked abilities: HotkeyType -> set of owner IDs
        self._blocked_abilities: dict[HotkeyType, set[int]] = {}

        # Track current hotkeys for each blocked ability: HotkeyType -> list of keys
        self._current_hotkeys: dict[HotkeyType, list[str]] = {}

        self._monitor_thread = threading.Thread(target=self._hotkey_monitor, daemon=True)
        self._monitor_thread.start()

    def disable_ability(self, ability: HotkeyType, owner: int):
        """Request to block an ability. Keys are blocked per-owner."""
        with self._lock:
            if ability not in self._blocked_abilities:
                self._blocked_abilities[ability] = set()
            self._blocked_abilities[ability].add(owner)

            hotkey = self._get_hotkey_for_ability(ability)
            if hotkey:
                self._current_hotkeys[ability] = hotkey
                for key in hotkey:
                    self._keyboard_controller.block_key(key)
                self._game_overlay.show_aility_cover(ability)

    def enable_ability(self, ability: HotkeyType, owner: int):
        """Release a block request for an ability."""
        with self._lock:
            if ability not in self._blocked_abilities:
                return

            self._blocked_abilities[ability].discard(owner)

            if self._blocked_abilities[ability]:
                return

            del self._blocked_abilities[ability]

            hotkey = self._current_hotkeys.get(ability)
            if hotkey:
                for key in hotkey:
                    self._keyboard_controller.unblock_key(key)
                self._game_overlay.hide_aility_cover(ability)
                del self._current_hotkeys[ability]

    def _get_hotkey_for_ability(self, ability: HotkeyType) -> Optional[list[str]]:
        """Get the current hotkey for an ability from the live client config."""
        config = self._live_client_config_fetcher.fetch()
        if not config:
            return None

        return getattr(config.input, ability.value, None)

    def _hotkey_monitor(self):
        """Monitor for hotkey changes and update blocked keys accordingly."""
        while True:
            with self._lock:
                for ability in self._blocked_abilities.keys():
                    self._update_hotkey_if_changed(ability)
            time.sleep(0.5)

    def _update_hotkey_if_changed(self, ability: HotkeyType):
        """Update blocked keys if the hotkey for an ability has changed."""
        new_hotkey = self._get_hotkey_for_ability(ability)
        old_hotkey = self._current_hotkeys.get(ability)

        if not new_hotkey or new_hotkey == old_hotkey:
            return

        owners = self._blocked_abilities.get(ability)
        if not owners:
            return

        if old_hotkey:
            for key in old_hotkey:
                self._keyboard_controller.unblock_key(key)

        for key in new_hotkey:
            self._keyboard_controller.block_key(key)

        self._current_hotkeys[ability] = new_hotkey
