from ..lol_data.active_player_data import ActivePlayerData
from ..utils.constants import Constants


class ResouceBase:
    resource_num: int

    overlay_types = {Constants.RESOURCE: []}

    @classmethod
    def check_dependencies(cls):
        if cls.resource_num == 0:
            return True
        else:
            resource_type = cls.get_resource_data()["type"]
            return resource_type in ("MANA", "ENERGY")

    @classmethod
    def get_resource_data(cls):
        if cls.resource_num == 0:
            type = None
            max = ActivePlayerData.get_champion_stat("maxHealth")
            value = ActivePlayerData.get_champion_stat("currentHealth")
        elif cls.resource_num == 1:
            type = ActivePlayerData.get_champion_stat("resourceType")
            max = ActivePlayerData.get_champion_stat("resourceMax")
            value = ActivePlayerData.get_champion_stat("resourceValue")

        return {"type": type, "max": max, "value": value}

    @classmethod
    def get_resource_diff(cls):
        resource_data = cls.get_resource_data()
        resource_diff = resource_data["max"] - resource_data["value"]

        return resource_diff

    @classmethod
    def get_percent(cls, resource_data: dict):
        percent = resource_data["value"] / resource_data["max"]

        return percent

    @classmethod
    def set_overlay_type(cls, *args: tuple[Constants, list[tuple[int, float | int]]]):
        for overlay_types in args:
            overlay_type = overlay_types[0]
            overlay_nums = overlay_types[1]

            cls.overlay_types[overlay_type] = overlay_nums
