from .resource_quest_base import ResourceQuestBase
from ..utils.constants import Constants


class DontTakeDmg(ResourceQuestBase):
    title = "Dont take damage!"
    difficulty = 0
    attributes = [Constants.RESOURCE]

    resource_num = 0
