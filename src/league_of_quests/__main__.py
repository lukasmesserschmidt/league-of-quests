import time
import keyboard

from .engine import QuestManager
from .core import GameDisruptor, HotkeyType
from .data import LiveClientConfigMonitor


def main():
    manager = QuestManager()
    manager.start()


if __name__ == "__main__":
    main()
