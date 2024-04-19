import json

from .get_lol_settings_path import get_lol_settings_path
from ..utils.lol_settings_converter import convert_hotkey


class LolSettings:

    @classmethod
    def import_settings(cls):
        with open(get_lol_settings_path(), "r") as f:
            all_lol_settings = json.load(f)
        return all_lol_settings

    @classmethod
    def get_map_scale(cls):
        return float(
            cls.import_settings()["files"][0]["sections"][5]["settings"][23]["value"]
        )

    @classmethod
    def get_global_scale(cls):
        return float(
            cls.import_settings()["files"][0]["sections"][5]["settings"][14]["value"]
        )

    @classmethod
    def get_ability_hotkey(cls, ability_num):
        return convert_hotkey(
            cls.import_settings()["files"][1]["sections"][0]["settings"][
                8 + ability_num
            ]["value"]
        )

    @classmethod
    def get_summoner_spell_hotkey(cls, summoner_spell_num):
        return convert_hotkey(
            cls.import_settings()["files"][1]["sections"][0]["settings"][
                6 + summoner_spell_num
            ]["value"]
        )

    @classmethod
    def get_trinket_hotkey(cls):
        return convert_hotkey(
            cls.import_settings()["files"][1]["sections"][0]["settings"][167]["value"]
        )

    @classmethod
    def get_teleport_hotkey(cls):
        return convert_hotkey(
            cls.import_settings()["files"][1]["sections"][0]["settings"][166]["value"]
        )
