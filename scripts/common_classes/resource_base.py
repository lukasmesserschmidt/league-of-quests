"""
This module contains the Base class for all resource quests or restrictions.
"""

from ..common_classes.enable_overlay_base import EnableOverlayBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.constants import Constants


class ResouceBase(EnableOverlayBase):
    """
    This class is the base class for all resource quests or restrictions.
    """

    # init variables
    resource_num: int

    overlay_types = {Constants.RESOURCE: []}

    @classmethod
    def check_dependencies(cls):
        """
        Checks if the quest or restriction is ready to start.
        """
        if cls.resource_num == 0:
            return True
        else:
            resource_type = cls.get_resource_data()["type"]
            return resource_type in ("MANA", "ENERGY")

    @classmethod
    def get_resource_data(cls):
        """
        Gets the resource data.

        returns: type, max, value of the resource if available
        """
        if cls.resource_num == 0:
            resource_type = None
            resource_max = ActivePlayerData.get_champion_stat("maxHealth")
            resource_value = ActivePlayerData.get_champion_stat("currentHealth")
        elif cls.resource_num == 1:
            resource_type = ActivePlayerData.get_champion_stat("resourceType")
            resource_max = ActivePlayerData.get_champion_stat("resourceMax")
            resource_value = ActivePlayerData.get_champion_stat("resourceValue")

        return {"type": resource_type, "max": resource_max, "value": resource_value}

    @classmethod
    def get_resource_diff(cls):
        """
        Gets the resource diff between max and value.
        """
        resource_data = cls.get_resource_data()
        resource_diff = resource_data["max"] - resource_data["value"]

        return resource_diff

    @classmethod
    def get_percent(cls, resource_data: dict[str, float, float]):
        """
        Gets the percent of the current value in comparison to max.
        """
        percent = resource_data["value"] / resource_data["max"]

        return percent
