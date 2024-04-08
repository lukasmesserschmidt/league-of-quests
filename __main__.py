from .gui import main_menu
from .gui import quest_display, quest_display_frame

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt


a = QApplication(sys.argv)
d = quest_display.QuestDisplay()
f = quest_display_frame.QuestDisplayFrame()
d.display.scroll_area_vertical_Layout.addWidget(f, 0, Qt.AlignRight | Qt.AlignTop)
f = quest_display_frame.QuestDisplayFrame()
d.display.scroll_area_vertical_Layout.addWidget(f, 0, Qt.AlignRight | Qt.AlignTop)
f = quest_display_frame.QuestDisplayFrame()
d.display.scroll_area_vertical_Layout.addWidget(f, 0, Qt.AlignRight | Qt.AlignTop)
f = quest_display_frame.QuestDisplayFrame()
d.display.scroll_area_vertical_Layout.addWidget(f, 0, Qt.AlignRight | Qt.AlignTop)

d.show()
a.exec()
# main_menu.MainWindow()
