from .quest_base import QuestBase
from ..gui.game_overlay.game_overlay_window import get_game_overlay


class ResourceQuestBase(QuestBase):
    resource_num: int

    @classmethod
    def init(cls):
        cls.duration = cls.get_duration(1 / 9)
        cls.finish_color_enabled = True
        cls.last_resource_diff = cls.get_resource_diff()

    @classmethod
    def quest_content(cls):
        resource_data = cls.get_resource_data()

        percent = resource_data["value"] / resource_data["max"]
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
    def get_resource_data(
        cls, type: str = None, max: float = None, value: float = None
    ):
        return {"type": type, "max": max, "value": value}

    @classmethod
    def get_resource_diff(cls):
        resource_data = cls.get_resource_data()
        resource_diff = resource_data["max"] - resource_data["value"]

        return resource_diff

    @classmethod
    def get_overlay_type(cls, percent: float):
        return {"resource": [(cls.resource_num, percent)]}
