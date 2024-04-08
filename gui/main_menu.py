import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from threading import Thread
import time

from .quest_tab_frames import (
    GeneralSettings,
    EasyQuestSettings,
    MidQuestSettings,
    HardQuestSettings,
)
from .quest_display import QuestDisplay
from ..quests.quests_manager import QuestManager
from ..settings_manager import Settings
from .. import constants


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # config
        self.geometry("500x700")
        # self.set_geometry()
        # self.resizable(False, False)
        self.attributes("-topmost", True)
        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure((0), weight=1)

        # visual
        self.title("League of Quests")
        self.iconbitmap(default="lol_quest/graphics/loq_icon.ico")

        self._set_appearance_mode("dark")

        # default_font = ("Arial", 16)
        # self.option_add("*Font", default_font)

        # settings
        Settings.import_settings()
        Settings.convert_settings()

        # start overlay
        self.start_overlay = StartOerlay(self)

        # tab view
        self.tab_view = TabView(self)

        # main loop
        self.mainloop()

    def set_geometry(self):
        base_geometry = (800, 1000)
        base_res = (3840, 2160)
        current_res = (self.winfo_screenwidth(), self.winfo_screenheight())
        geometry = []
        for i, (b_res, c_res) in enumerate(zip(base_res, current_res)):
            res = int(c_res / b_res * base_geometry[i])
            geometry.append(res)
        self.geometry("%dx%d" % tuple(geometry))


class StartOerlay(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # place
        self.grid(row=1, column=0, padx=10, pady=2, sticky="nsew")

        # config
        self.configure(height=50, fg_color=constants.FG_COLOR)

        # create widgets
        self.create_widgets()

    def create_widgets(self):
        start_button = ctk.CTkButton(self, text="Start", command=self.start)
        start_button.place(relx=0.95, rely=0.5, anchor="e")

    def start(self):
        QuestDisplay()


class TabView(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, padx=10, pady=2, sticky="nsew")

        # tabs
        self.add(name="Quest Settings")
        self.add(name="Impairments Settings")

        self.quest_settings = QuestsTab(self.tab("Quest Settings"))
        self.impairments_settings = self.tab("Impairments Settings")

        # colors
        self.text_color = "#ffffff"
        self.segment_color = "#222222"


class QuestsTab(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        # place
        self.pack(fill="both", expand=True)

        # config
        self.grid_rowconfigure((0, 1, 2), weight=0, pad=10)
        self.grid_columnconfigure((0), weight=1, pad=5)

        # create widgets
        self.create_widgets()

    def create_widgets(self):
        general_settings = GeneralSettings(self)
        general_settings.grid(row=0, column=0, sticky="new")

        easy_quest_settings = EasyQuestSettings(self)
        easy_quest_settings.grid(row=1, column=0, sticky="new")

        easy_quest_settings = MidQuestSettings(self)
        easy_quest_settings.grid(row=2, column=0, sticky="new")

        easy_quest_settings = HardQuestSettings(self)
        easy_quest_settings.grid(row=3, column=0, sticky="new")


class ImpairmentsTab(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master.tab_view.tab("Impairments Settings"))
