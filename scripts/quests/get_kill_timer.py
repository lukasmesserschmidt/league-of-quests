from .timer_quest_base import TimerQuestBase
from ..lol_data.active_player_data import ActivePlayerData
from ..utils.constants import Constants


class GetKillTimer(TimerQuestBase):
    title = "Get one kill or timer x2!"
    difficulty = 2
    attributes = [Constants.KILL, Constants.TIMER]

    get_stat_func = ActivePlayerData.get_kills

    @classmethod
    def complete_condition(cls, current_stat):
        return cls.last_stat < current_stat
