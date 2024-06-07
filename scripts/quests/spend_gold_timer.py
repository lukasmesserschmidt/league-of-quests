from .timer_quest_base import TimerQuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.constants import Constants


class SpendGoldTimer(TimerQuestBase):
    title = "Spend gold or timer x2!"
    difficulty = 1
    attributes = [Constants.GOLD, Constants.TIMER]

    get_stat_func = ActivePlayerData.get_current_gold

    @classmethod
    def complete_condition(cls, current_stat):
        return current_stat < cls.last_stat
