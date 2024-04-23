from .manager_base import ManagerBase
from ..quests import all_quests


class QuestManager(ManagerBase):
    object_type = "quest"
    all_objects = all_quests

    active_objects = []
