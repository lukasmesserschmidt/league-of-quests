from .quest_base import QuestBase
from ..lol_data.active_player_data import AcitvePlayerData
from ..gui.game_overlay.game_overlay_window import get_game_overlay
from ..utils.attributes import RESOURCE


class DontSpendResources(QuestBase):
    title = "Dont spend ?!"
    difficulty = 1
    attributes = [RESOURCE]

    @classmethod
    def check_dependencies(cls):
        resource_data = AcitvePlayerData.get_resource_data()

        if resource_data["type"] == "MANA" or resource_data["type"] == "ENERGY":
            return True

    @classmethod
    def init(cls):
        cls.duration = cls.get_duration(1 / 9)
        cls.finish_color_enabled = True
        resource_data = AcitvePlayerData.get_resource_data()
        cls.title = f"Dont spend {resource_data["type"]}!"
        cls.last_resource_diff = resource_data["max"] - resource_data["value"]

    @classmethod
    def quest_content(cls):
        resource_data = AcitvePlayerData.get_resource_data()
        current_resource_diff = resource_data["max"] - resource_data["value"]

        percent = resource_data["value"] / resource_data["max"]
        get_game_overlay().enable_cover(True, "resource", (1, percent))

        if cls.last_resource_diff < current_resource_diff:
            cls.last_resource_diff = current_resource_diff
            
            cls.end_time = cls.get_end_time(cls.duration)

        cls.last_resource_diff = current_resource_diff
    
    @classmethod
    def on_end(cls):
        get_game_overlay().enable_cover(False, "resource", 1)
