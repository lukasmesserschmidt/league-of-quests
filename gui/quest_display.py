from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QCursor
import keyboard

# import customtkinter as ctk
# import win32gui
# import win32con

from .quest_display_base import Ui_QuestDisplay


# class QuestDisplay1(ctk.CTkToplevel):
#     def __init__(self):
#         super().__init__()
#         self.geometry("300x300")
#         self.wm_attributes("-transparentcolor", "white", "-topmost", True)
#         self.overrideredirect(True)
#         self.configure(fg_color="white")

#         frame = ctk.CTkFrame(self, fg_color="white", width=300, height=100)
#         frame.pack()

#         label = ctk.CTkLabel(
#             frame,
#             text="test",
#             fg_color=constants.EASY_COLOR,
#             text_color="white",
#             width=70,
#             height=50,
#             corner_radius=10,
#         )
#         label.pack()

#         self.make_clickthrough(frame.winfo_id())

#     def make_clickthrough(self, hwnd):
#         try:
#             styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
#             styles |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
#             win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
#             win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
#         except Exception as e:
#             print(e)


class QuestDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000, 1000, 250, 300)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint
            | Qt.WindowTransparentForInput
            | Qt.FramelessWindowHint
        )

        self.ui = Ui_QuestDisplay()
        self.ui.setupUi(self)

        self.move_timer = QTimer(self)
        self.move_timer.timeout.connect(self.move_to_mouse)
        self.move_timer.start(10)

    def move_to_mouse(self):
        if keyboard.is_pressed("shift"):
            x = QCursor.pos().toTuple()[0] - self.width() / 2
            y = QCursor.pos().toTuple()[1]
            self.move(x, y)
