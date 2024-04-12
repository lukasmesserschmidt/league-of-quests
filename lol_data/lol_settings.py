from .get_lol_settings import GetLolSettings


class LolSettings:
    GetLolSettings.get_lol_settings_path()
    GetLolSettings.import_lol_settings()

    @classmethod
    def get_map_scale(cls):
        return float(
            GetLolSettings.all_lol_settings["files"][0]["sections"][5]["settings"][23][
                "value"
            ]
        )
