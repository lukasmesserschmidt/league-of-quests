from .engine.quest_manager import QuestManager


def main():
    quest_manager = QuestManager()
    quest_manager.loop()


if __name__ == "__main__":
    main()
