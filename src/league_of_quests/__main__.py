from PySide6.QtWidgets import QApplication

from .engine import AppController


def main():
    app = QApplication([])
    app.setApplicationName("League of Quests")

    controller = AppController()

    app.exec()


if __name__ == "__main__":
    main()
