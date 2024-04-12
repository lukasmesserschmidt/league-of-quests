import sys
from PySide6.QtWidgets import QApplication


def create_app():
    global app

    app = QApplication(sys.argv)


def start():
    app.exec()
