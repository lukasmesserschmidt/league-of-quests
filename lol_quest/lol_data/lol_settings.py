from .get_lol_settings import GetLolSettings
from ..utils.hotkey_converter import convert_hotkey


class LolSettings:
    lol_settings = {
        # general
        "flip_map": lambda: int(
            GetLolSettings.all_lol_settings.get("files")[0]
            .get("sections")[5]
            .get("settings")[13]
            .get("value")
        ),
        "map_scale": lambda: float(
            GetLolSettings.all_lol_settings.get("files")[0]
            .get("sections")[5]
            .get("settings")[23]
            .get("value")
        ),
        "global_scale": lambda: float(
            GetLolSettings.all_lol_settings.get("files")[0]
            .get("sections")[5]
            .get("settings")[14]
            .get("value")
        ),
        "window_mode": lambda: int(
            GetLolSettings.game_cfg.get("General", "WindowMode")
        ),
        "width": lambda: int(GetLolSettings.game_cfg.get("General", "Width")),
        "height": lambda: int(GetLolSettings.game_cfg.get("General", "Height")),
        # hotkeys
        "ability": lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[8 + num]
            .get("value")
        ),
        "quick_ability": lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[112 + num]
            .get("value")
        ),
        "summoner_spell": lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[6 + num]
            .get("value")
        ),
        "quick_summoner_spell": lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[104 + num]
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
        "snap_cam": lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[5]
            .get("value")
        ),
    }

    @classmethod
    def get_lol_setting(cls, setting: str, *args):
        setting = cls.lol_settings[setting](*args)
        return setting

    @classmethod
    def get_hotkeys(cls, hotkey_types: dict[str, list[int]]):
        hotkeys = []
        for hotkey_type, args in hotkey_types.items():
            for arg in args:
                if type(arg) != tuple:
                    hotkey = cls.get_lol_setting(hotkey_type, arg)
                else:
                    hotkey = tuple(
                        [cls.get_lol_setting(hotkey_type, key) for key in arg]
                    )
                hotkeys.append(hotkey)

        return hotkeys
