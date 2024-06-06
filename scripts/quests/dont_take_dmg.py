from .resource_quest_base import ResourceQuestBase

from ..utils.attributes import RESOURCE


class DontTakeDmg(ResourceQuestBase):
    title = "Dont take damage!"
    difficulty = 0
    attributes = [RESOURCE]

    resource_num = 0
