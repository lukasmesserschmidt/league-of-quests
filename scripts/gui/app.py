import sys
from PySide6.QtWidgets import QApplication


def create_app():
    global app
    app = QApplication(sys.argv)


def get_app():
    return app


def start():
    sys.exit(app.exec_())
