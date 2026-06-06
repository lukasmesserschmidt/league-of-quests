from PySide6.QtWidgets import QApplication

from .engine import QuestManager


def main():
    app = QApplication([])
    app.setApplicationName("League of Quests")

    manager = QuestManager()
    manager.start()

    app.exec()


if __name__ == "__main__":
    main()
