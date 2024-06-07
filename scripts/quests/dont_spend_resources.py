from .resource_quest_base import ResourceQuestBase
from ..utils.constants import Constants


class DontSpendResources(ResourceQuestBase):
    title = "Dont spend ?!"
    difficulty = 1
    attributes = [Constants.RESOURCE]

    resource_num = 1

    @classmethod
    def init(cls):
        super().init()
        resource_type = cls.get_resource_data()["type"]
        cls.title = f"Dont spend {resource_type}!"
