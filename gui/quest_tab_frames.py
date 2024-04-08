from .frame_base import FrameBase

from .. import constants
from . import widget_creators as wc
from ..settings_manager import Settings


class GeneralSettings(FrameBase):
    def __init__(self, master):
        super().__init__(master)

        self.create_headline("General Settings")
        self.create_content()

    def create_content(self):
        # base
        super().create_content()

        self.content_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.content_frame.grid_columnconfigure((0, 1, 2), weight=1)

        general_s = Settings.all_settings["general"]

        # widgets
        wc.general_sw(
            self.content_frame,
            "First Quest Available at",
            general_s["firstquest"],
            unit="seconds",
            row=0,
        )

        wc.general_sw(
            self.content_frame,
            "General Quest Duration",
            general_s["questduration"],
            unit="x",
            row=1,
        )

        wc.general_sw(
            self.content_frame,
            "General Completion Duration",
            general_s["completionduration"],
            unit="x",
            row=2,
        )


class EasyQuestSettings(FrameBase):
    def __init__(self, master):
        super().__init__(master)

        self.create_headline("Easy Quest Settings")
        self.create_content()

    def create_content(self):
        # base
        super().create_content(2)

        self.content_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.content_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        easy_quests_s = Settings.all_settings["quests"]["easy"]
        general_s = Settings.all_settings["general"]

        # widgets
        wc.quest_sw(
            self.content_frame,
            "test",
            easy_quests_s["test"],
            general_s["questduration"],
            competion_duration_scale_var=general_s["completionduration"],
            row=0,
        )


class MidQuestSettings(FrameBase):
    def __init__(self, master):
        super().__init__(master)

        self.create_headline("Mid Quest Settings")
        self.create_content()

    def create_content(self):
        # base
        super().create_content(2)

        self.content_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.content_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        easy_quests_s = Settings.all_settings["quests"]["mid"]
        general_s = Settings.all_settings["general"]

        # widgets
        wc.quest_sw(
            self.content_frame,
            "test",
            easy_quests_s["test"],
            general_s["questduration"],
            competion_duration_scale_var=general_s["completionduration"],
            row=0,
        )


class HardQuestSettings(FrameBase):
    def __init__(self, master):
        super().__init__(master)

        self.create_headline("Hard Quest Settings")
        self.create_content()

    def create_content(self):
        # base
        super().create_content(2)

        self.content_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.content_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        easy_quests_s = Settings.all_settings["quests"]["hard"]
        general_s = Settings.all_settings["general"]

        # widgets
        wc.quest_sw(
            self.content_frame,
            "test",
            easy_quests_s["test"],
            general_s["questduration"],
            competion_duration_scale_var=general_s["completionduration"],
            row=0,
        )
