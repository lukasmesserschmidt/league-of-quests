import json
import customtkinter as ctk


class Settings:
    all_settings: dict

    @classmethod
    def import_settings(cls):
        with open("lol_quest/settings.json", "r") as f:
            data = json.load(f)
        cls.all_settings = data

    @classmethod
    def convert_settings(cls):
        for name, value in cls.all_settings["general"].items():
            cls.all_settings["general"][name] = ctk.StringVar(value=value)

        for difficulty in cls.all_settings["quests"].values():
            for value in difficulty.values():
                value["unlocked"] = ctk.IntVar(value=value["unlocked"])
                value["questduration"] = ctk.StringVar(value=value["questduration"])
                value["completionduration"] = ctk.StringVar(value=value["completionduration"])
        