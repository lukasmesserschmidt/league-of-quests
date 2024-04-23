from .manager_base import ManagerBase
from ..restrictions import all_restrictions


class RestrictionManager(ManagerBase):
    object_type = "restriction"
    all_objects = all_restrictions

    active_objects = []
