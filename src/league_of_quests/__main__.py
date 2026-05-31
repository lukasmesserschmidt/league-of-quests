import time

from .engine import QuestManager
from .data.live_client_config_monitor import LiveClientConfigMonitor


def main():
    config_monitor = LiveClientConfigMonitor()
    # manager = QuestManager()
    # manager.loop()

    while True:
        config = config_monitor.get_config()
        print(config)
        time.sleep(1)


if __name__ == "__main__":
    main()
