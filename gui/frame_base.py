import customtkinter as ctk

from .. import constants


class FrameBase(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0), weight=1)

    def create_headline(
        self,
        text: str,
        fg_color: str = constants.FG_COLOR,
        text_color: str = constants.TEXT_COLOR,
        row=0,
    ):
        headline_frame = ctk.CTkFrame(self, fg_color=fg_color, height=30)
        headline_label = ctk.CTkLabel(headline_frame, text=text, text_color=text_color)

        headline_frame.grid(row=row, column=0, sticky="new")
        headline_label.place(relx=0.5, rely=0.5, anchor="center")

    def create_content(self, row=1):
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=row, column=0, sticky="new")
