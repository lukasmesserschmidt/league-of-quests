import time
import keyboard

from .engine import QuestManager
from .core import GameDisruptor, HotkeyType
from .data import LiveClientConfigMonitor


def main():
    # manager = QuestManager()
    # manager.start()

    live_client_config_monitor = LiveClientConfigMonitor()
    disruptor = GameDisruptor(live_client_config_monitor)
    disruptor.disable_ability(HotkeyType.ABILITY_1, 1)
    disruptor.disable_ability(HotkeyType.ABILITY_2, 2)
    print(disruptor._blocked_abilities)
    print(disruptor._keyboard_controller._key_ref_counts)
    time.sleep(5)
    disruptor.enable_ability(HotkeyType.ABILITY_1, 1)
    print(disruptor._blocked_abilities)
    print(disruptor._keyboard_controller._key_ref_counts)
    time.sleep(5)
    disruptor.enable_ability(HotkeyType.ABILITY_2, 2)
    print(disruptor._blocked_abilities)
    print(disruptor._keyboard_controller._key_ref_counts)
    time.sleep(500)


if __name__ == "__main__":
    main()
