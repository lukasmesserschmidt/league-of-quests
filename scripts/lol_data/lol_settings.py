from .get_lol_settings import GetLolSettings
from ..utils.hotkey_converter import convert_hotkey
from ..utils.constants import Constants


class LolSettings:
    lol_settings = {
        # general
        Constants.FLIP_MAP: lambda: int(
            GetLolSettings.all_lol_settings.get("files")[0]
            .get("sections")[5]
            .get("settings")[13]
            .get("value")
        ),
        Constants.MAP_SCALE: lambda: float(
            GetLolSettings.all_lol_settings.get("files")[0]
            .get("sections")[5]
            .get("settings")[23]
            .get("value")
        ),
        Constants.GLOBAL_SCALE: lambda: float(
            GetLolSettings.all_lol_settings.get("files")[0]
            .get("sections")[5]
            .get("settings")[14]
            .get("value")
        ),
        Constants.WINDOW_MODE: lambda: int(
            GetLolSettings.game_cfg.get("General", "WindowMode")
        ),
        Constants.WIDTH: lambda: int(GetLolSettings.game_cfg.get("General", "Width")),
        Constants.HEIGHT: lambda: int(GetLolSettings.game_cfg.get("General", "Height")),
        # hotkeys
        Constants.ABILITY: lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[8 + num]
            .get("value")
        ),
        Constants.QUICK_ABILITY: lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[112 + num]
            .get("value")
        ),
        Constants.LEVEL_ABILITY: lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[22 + num]
            .get("value")
        ),
        Constants.SUMMONER_SPELL: lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[6 + num]
            .get("value")
        ),
        Constants.QUICK_SUMMONER_SPELL: lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[104 + num]
            .get("value")
        ),
        Constants.TRINKET: lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[167]
            .get("value")
        ),
        Constants.TELEPORT: lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[166]
            .get("value")
        ),
        Constants.SELECT_ALLY: lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[77 + num]
            .get("value")
        ),
        Constants.SNAP_CAM: lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[5]
            .get("value")
        ),
        Constants.STOP_POSITION: lambda num: convert_hotkey(
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")[59]
            .get("value")
        ),
    }

    @classmethod
    def get_lol_setting(cls, setting: Constants, *args):
        setting = cls.lol_settings[setting](*args)
        return setting

    @classmethod
    def get_hotkeys(cls, hotkey_types: dict[Constants, list[int]]):
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
