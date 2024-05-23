from .resource_quest_base import ResourceQuestBase
from ..lol_data.active_player_data import ActivePlayerData

from ..utils.attributes import RESOURCE


class DontTakeDmg(ResourceQuestBase):
    title = "Dont take damage!"
    difficulty = 0
    resource_num = 0
    attributes = [RESOURCE]

    @classmethod
    def get_resource_data(cls):
        max_health = ActivePlayerData.get_champion_stat("maxHealth")
        current_health = ActivePlayerData.get_champion_stat("currentHealth")

        return super().get_resource_data(max=max_health, value=current_health)
