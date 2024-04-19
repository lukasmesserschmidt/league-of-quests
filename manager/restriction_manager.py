from .manager_base import ManagerBase
from ..restrictions.disable_ability_0 import DisableAbility0
from ..restrictions.disable_ability_3 import DisableAbility3


class RestrictionManager(ManagerBase):
    object_type = "restriction"
    all_objects = [
        DisableAbility0,
        DisableAbility3,
    ]

    active_objects = []
