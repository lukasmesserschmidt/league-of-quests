from .quest_base import QuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..gui.game_overlay.game_overlay_window import get_game_overlay
from ..utils.attributes import RESOURCE


class DontSpendResources(QuestBase):
    title = "Dont spend ?!"
    difficulty = 1
    attributes = [RESOURCE]

    @classmethod
    def check_dependencies(cls):
        resource_type, _, _ = cls.get_resource_data()

        if resource_type == "MANA" or resource_type == "ENERGY":
            return True

    @classmethod
    def init(cls):
        cls.duration = cls.get_duration(1 / 9)
        cls.finish_color_enabled = True
        resource_type, _, _ = cls.get_resource_data()
        cls.title = f"Dont spend {resource_type}!"
        cls.last_resource_diff = cls.get_resource_diff()

    @classmethod
    def quest_content(cls):
        _, resource_max, resource_value = cls.get_resource_data()

        percent = resource_value / resource_max
        get_game_overlay().enable_cover(True, cls.get_overlay_type(percent))

        current_resource_diff = cls.get_resource_diff()

        if cls.last_resource_diff < current_resource_diff:
            cls.last_resource_diff = current_resource_diff

            cls.end_time = cls.get_end_time(cls.duration)

        cls.last_resource_diff = current_resource_diff

    @classmethod
    def on_end(cls):
        get_game_overlay().enable_cover(False, cls.get_overlay_type(1))

    @classmethod
    def get_resource_diff(cls):
        _, resource_max, resource_value = cls.get_resource_data()
        resource_diff = resource_max - resource_value

        return resource_diff

    @classmethod
    def get_resource_data(cls):
        resource_type = ActivePlayerData.get_champion_stat("resourceType")
        resource_max = ActivePlayerData.get_champion_stat("resourceMax")
        resource_value = ActivePlayerData.get_champion_stat("resourceValue")

        return resource_type, resource_max, resource_value

    @classmethod
    def get_overlay_type(cls, percent: float):
        return {"resource": [(1, percent)]}
