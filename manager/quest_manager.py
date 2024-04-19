from .manager_base import ManagerBase
from ..quests.have_low_gold import HaveLowGold
from ..quests.spend_gold_timer import SpendGoldTimer


class QuestManager(ManagerBase):
    object_type = "quest"
    all_objects = [
        HaveLowGold,
        SpendGoldTimer,
    ]

    active_objects = []
