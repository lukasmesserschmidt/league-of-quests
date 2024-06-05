from .get_lol_settings import GetLolSettings
from ..utils.constants import Constants
from ..utils import user_data


class LolSettings:
    lol_settings = {
        # general
        Constants.FLIP_MAP: lambda: int(
            LolSettings._find_setting(
                LolSettings._get_general_settings(),
                "FlipMiniMap",
                0,
            )
        ),
        Constants.MAP_SCALE: lambda: float(
            LolSettings._find_setting(
                LolSettings._get_general_settings(),
                "MinimapScale",
                1,
            )
        ),
        Constants.GLOBAL_SCALE: lambda: float(
            LolSettings._find_setting(
                LolSettings._get_general_settings(),
                "GlobalScale",
                1,
            )
        ),
        Constants.WINDOW_MODE: lambda: int(
            LolSettings._get_game_cfg_setting("General", "WindowMode", 0)
        ),
        Constants.WIDTH: lambda: int(
            LolSettings._get_game_cfg_setting(
                "General", "Width", user_data.get_monitor_resolution()[0]
            )
        ),
        Constants.HEIGHT: lambda: int(
            LolSettings._get_game_cfg_setting(
                "General", "Height", user_data.get_monitor_resolution()[1]
            )
        ),
        # hotkeys
        Constants.ABILITY: lambda num: LolSettings._find_setting(
            LolSettings._get_hotkey_settings(),
            f"evtCastSpell{num + 1}",
            "",
            True,
        ),
        Constants.QUICK_ABILITY: lambda num: LolSettings._find_setting(
            LolSettings._get_hotkey_settings(),
            f"evtSmartCastSpell{num + 1}",
            "",
            True,
        ),
        Constants.LEVEL_ABILITY: lambda num: LolSettings._find_setting(
            LolSettings._get_hotkey_settings(),
            f"evtLevelSpell{num + 1}",
            "",
            True,
        ),
        Constants.SUMMONER_SPELL: lambda num: LolSettings._find_setting(
            LolSettings._get_hotkey_settings(),
            f"evtCastAvatarSpell{num + 1}",
            "",
            True,
        ),
        Constants.QUICK_SUMMONER_SPELL: lambda num: LolSettings._find_setting(
            LolSettings._get_hotkey_settings(),
            f"evtSmartCastAvatarSpell{num + 1}",
            "",
            True,
        ),
        Constants.TRINKET: lambda num: LolSettings._find_setting(
            LolSettings._get_hotkey_settings(),
            "evtUseVisionItem",
            "",
            True,
        ),
        Constants.TELEPORT: lambda num: LolSettings._find_setting(
            LolSettings._get_hotkey_settings(),
            "evtUseItem7",
            "",
            True,
        ),
        Constants.SELECT_ALLY: lambda num: LolSettings._find_setting(
            LolSettings._get_hotkey_settings(),
            f"evtSelectAlly{num + 1}",
            "",
            True,
        ),
        Constants.SNAP_CAM: lambda num: LolSettings._find_setting(
            LolSettings._get_hotkey_settings(),
            "evtCameraSnap",
            "",
            True,
        ),
        Constants.STOP_POSITION: lambda num: LolSettings._find_setting(
            LolSettings._get_hotkey_settings(),
            "evtPlayerStopPosition",
            "",
            True,
        ),
    }

    @classmethod
    def get_lol_setting(cls, setting: Constants, *args):
        setting = cls.lol_settings[setting](*args)
        return setting

    @classmethod
    def get_hotkeys(cls, hotkey_types: set[tuple[Constants, int | tuple[int, int]]]):
        hotkeys = set()
        for hotkey_type in hotkey_types:
            if type(hotkey_type[1]) == tuple:
                hotkey = tuple(
                    [cls.get_lol_setting(hotkey_type[0], num) for num in hotkey_type[1]]
                )
            else:
                hotkey = cls.get_lol_setting(hotkey_type[0], hotkey_type[1])
            hotkeys.add(hotkey)

        return hotkeys

    # utils
    @staticmethod
    def _get_general_settings():
        return (
            GetLolSettings.all_lol_settings.get("files")[0]
            .get("sections")[5]
            .get("settings")
        )

    @staticmethod
    def _get_hotkey_settings():
        return (
            GetLolSettings.all_lol_settings.get("files")[1]
            .get("sections")[0]
            .get("settings")
        )

    @staticmethod
    def _get_game_cfg_setting(section: str, option: str, default):
        try:
            return GetLolSettings.game_cfg.get(section, option)
        except:
            return default

    @staticmethod
    def _find_setting(
        settings: list[dict], name: str, default, convert_hotkey: bool = False
    ):
        for setting in settings:
            if setting.get("name") == name:
                value = setting.get("value")
                if value is not None:
                    return (
                        LolSettings._convert_hotkey(value) if convert_hotkey else value
                    )
                else:
                    break

        return default

    @staticmethod
    def _convert_hotkey(hotkey: str):
        hotkey = hotkey.strip("[]")
        hotkey = hotkey.replace("][", "+")

        return hotkey
