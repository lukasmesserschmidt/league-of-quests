from .get_lol_settings import GetLolSettings
from ..utils.lol_settings_converter import convert_hotkey


class LolSettings:

    @classmethod
    def lol_settings(cls):
        return GetLolSettings.all_lol_settings

    @classmethod
    def get_map_scale(cls):
        return float(
            cls.lol_settings()["files"][0]["sections"][5]["settings"][23]["value"]
        )

    @classmethod
    def get_global_scale(cls):
        return float(
            cls.lol_settings()["files"][0]["sections"][5]["settings"][14]["value"]
        )

    @classmethod
    def get_ability_hotkey(cls, num):
        return convert_hotkey(
            cls.lol_settings()["files"][1]["sections"][0]["settings"][8 + num]["value"]
        )

    @classmethod
    def get_summoner_spell_hotkey(cls, num):
        return convert_hotkey(
            cls.lol_settings()["files"][1]["sections"][0]["settings"][6 + num]["value"]
        )

    @classmethod
    def get_trinket_hotkey(cls, num):
        return convert_hotkey(
            cls.lol_settings()["files"][1]["sections"][0]["settings"][167]["value"]
        )

    @classmethod
    def get_teleport_hotkey(cls, num):
        return convert_hotkey(
            cls.lol_settings()["files"][1]["sections"][0]["settings"][166]["value"]
        )

    @classmethod
    def get_level_ability_hotkey(cls, num):
        return convert_hotkey(
            cls.lol_settings()["files"][1]["sections"][0]["settings"][22 + num]["value"]
        )
