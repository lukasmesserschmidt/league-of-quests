from .quest_base import QuestBase
from ..common_classes.resource_base import ResouceBase
from ..gui.game_overlay.game_overlay_window import get_game_overlay
from ..utils.constants import Constants


class ResourceQuestBase(ResouceBase, QuestBase):

    @classmethod
    def init(cls):
        super().init(1 / 9)
        cls.finish_color_enabled = True
        cls.last_resource_diff = cls.get_resource_diff()

    @classmethod
    def quest_content(cls):
        resource_data = cls.get_resource_data()

        percent = cls.get_percent(resource_data)
        cls.set_overlay_type((Constants.RESOURCE, [(cls.resource_num, percent)]))
        get_game_overlay().enable_cover(True, cls.overlay_types)

        current_resource_diff = cls.get_resource_diff()

        if cls.last_resource_diff < current_resource_diff:
            cls.last_resource_diff = current_resource_diff

            cls.end_time = cls.get_end_time(cls.duration)

        cls.last_resource_diff = current_resource_diff

    @classmethod
    def on_end(cls):
        get_game_overlay().enable_cover(False, cls.overlay_types)
