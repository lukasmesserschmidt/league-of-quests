from .get_lol_settings import GetLolSettings
from ..utils.lol_settings_converter import convert_hotkey


class LolSettings:
    lol_settings = {
        "map_scale": lambda: GetLolSettings.all_lol_settings.get("files")[0]
        .get("sections")[5]
        .get("settings")[23]
        .get("value"),
        "global_scale": lambda: GetLolSettings.all_lol_settings.get("files")[0]
        .get("sections")[5]
        .get("settings")[14]
        .get("value"),
        "ability": lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[8 + num]
            .get("value")
        ),
        "summoner_spell": lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[6 + num]
            .get("value")
        ),
        "trinket": lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[167]
            .get("value")
        ),
        "teleport": lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[166]
            .get("value")
        ),
        "level_ability": lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[22 + num]
            .get("value")
        ),
    }

    @classmethod
    def get_hotkeys(cls, hotkey_type: str, *args: int):
        hotkeys = []
        for arg in args:
            hotkey = cls.lol_settings[hotkey_type](arg)
            hotkeys.append(hotkey)

        return hotkeys

    @classmethod
    def get_lol_settings(cls):
        return GetLolSettings.all_lol_settings

    @classmethod
    def get_map_scale(cls):
        return float(
            cls.get_lol_settings()["files"][0]["sections"][5]["settings"][23]["value"]
        )

    @classmethod
    def get_global_scale(cls):
        return float(
            cls.get_lol_settings()["files"][0]["sections"][5]["settings"][14]["value"]
        )

    @classmethod
    def get_ability_hotkey(cls, num):
        return convert_hotkey(
            cls.get_lol_settings()["files"][1]["sections"][0]["settings"][8 + num][
                "value"
            ]
        )

    @classmethod
    def get_summoner_spell_hotkey(cls, num):
        return convert_hotkey(
            cls.get_lol_settings()["files"][1]["sections"][0]["settings"][6 + num][
                "value"
            ]
        )

    @classmethod
    def get_trinket_hotkey(cls, num):
        return convert_hotkey(
            cls.get_lol_settings()["files"][1]["sections"][0]["settings"][167]["value"]
        )

    @classmethod
    def get_teleport_hotkey(cls, num):
        return convert_hotkey(
            cls.get_lol_settings()["files"][1]["sections"][0]["settings"][166]["value"]
        )

    @classmethod
    def get_level_ability_hotkey(cls, num):
        return convert_hotkey(
            cls.get_lol_settings()["files"][1]["sections"][0]["settings"][22 + num][
                "value"
            ]
        )
