from .quest_base import QuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..gui.game_overlay.game_overlay_window import get_game_overlay


class DontTakeDmg(QuestBase):
    title = "Dont take damage!"
    difficulty = 0
    attributes = []

    @classmethod
    def init(cls):
        cls.duration = cls.get_duration(1 / 9)
        cls.finish_color_enabled = True
        cls.last_health_diff = cls.get_health_diff()

    @classmethod
    def quest_content(cls):
        max_health, current_health = cls.get_health_data()

        percent = current_health / max_health
        get_game_overlay().enable_cover(True, cls.get_overlay_type(percent))

        current_health_diff = cls.get_health_diff()

        if cls.last_health_diff < current_health_diff:
            cls.end_time = cls.get_end_time(cls.duration)

        cls.last_health_diff = current_health_diff

    @classmethod
    def on_end(cls):
        get_game_overlay().enable_cover(False, cls.get_overlay_type(1))

    @classmethod
    def get_health_diff(cls):
        max_health, current_health = cls.get_health_data()
        health_diff = max_health - current_health

        return health_diff

    @classmethod
    def get_health_data(cls):
        max_health = ActivePlayerData.get_champion_stat("maxHealth")
        current_health = ActivePlayerData.get_champion_stat("currentHealth")

        return max_health, current_health

    @classmethod
    def get_overlay_type(cls, percent: float):
        return {"resource": [(0, percent)]}
