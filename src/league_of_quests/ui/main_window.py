from PySide6.QtCore import Qt, QFile, QIODevice
from PySide6.QtUiTools import QUiLoader


class MainWindow:
    def __init__(self):
        super().__init__()

        file = QFile(
            "C:\\dev\\league-of-quests\\src\\league_of_quests\\ui\\ui_files\\main_window.ui"
        )
        print(file.fileName())
        file.open(QIODevice.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file)
        file.close()
