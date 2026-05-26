from .engine import QuestManager


def main():
    manager = QuestManager()
    manager.loop()


if __name__ == "__main__":
    main()
