import time

from .quest_base import QuestBase
from ..lol_data.active_player_data import AcitvePlayerData
from ..gui.game_overlay.game_overlay_window import game_overlay
from ..utils.attributes import RESOURCE
from ..utils.top_window_is_lol import lol_is_top


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
    def on_start(cls):
        resource_data = AcitvePlayerData.get_resource_data()
        cls.title = f"Dont spend {resource_data["type"]}!"
        cls.last_resource_diff = resource_data["max"] - resource_data["value"]

    @classmethod
    def quest_loop(cls):
        multiplier = 1 / 9
        end_time = cls.get_end_time(multiplier)

        while time.time() < end_time:
            cls.remaining_time = end_time - time.time()
            if cls.quest_content():
                cls.finish_color_enabled = True
            else:
                end_time = cls.get_end_time(multiplier)
                cls.finish_color_enabled = False

            if cls.terminate_flag:
                break

        cls.terminate_flag = True

        cls.on_end()

    @classmethod
    def quest_content(cls):
        resource_data = AcitvePlayerData.get_resource_data()
        current_resource_diff = resource_data["max"] - resource_data["value"]

        if lol_is_top:
            percent = resource_data["value"] / resource_data["max"]
            game_overlay.resource_cover.show((1, percent))

        if cls.last_resource_diff < current_resource_diff:
            cls.last_resource_diff = current_resource_diff
            return False

        cls.last_resource_diff = current_resource_diff

        return True

    @classmethod
    def on_end(cls):
        game_overlay.resource_cover.hide(1)
