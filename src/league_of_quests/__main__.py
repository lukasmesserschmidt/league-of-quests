import time
import keyboard

from PySide6.QtWidgets import QApplication

from .ui import GameOverlayWindow


def main():
    app = QApplication([])
    app.setApplicationName("League of Quests")

    window = GameOverlayWindow()
    window.show()

    app.exec()

    # manager = QuestManager()
    # manager.start()


if __name__ == "__main__":
    main()
