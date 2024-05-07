from .resource_quest_base import ResourceQuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.attributes import RESOURCE


class DontSpendResources(ResourceQuestBase):
    title = "Dont spend ?!"
    difficulty = 1
    resource_num = 1
    attributes = [RESOURCE]

    @classmethod
    def check_dependencies(cls):
        resource_type = cls.get_resource_data()["type"]

        if resource_type == "MANA" or resource_type == "ENERGY":
            return True

    @classmethod
    def init(cls):
        super().init()
        resource_type = cls.get_resource_data()["type"]
        cls.title = f"Dont spend {resource_type}!"

    @classmethod
    def get_resource_data(cls):
        resource_type = ActivePlayerData.get_champion_stat("resourceType")
        resource_max = ActivePlayerData.get_champion_stat("resourceMax")
        resource_value = ActivePlayerData.get_champion_stat("resourceValue")

        return super().get_resource_data(
            type=resource_type, max=resource_max, value=resource_value
        )
