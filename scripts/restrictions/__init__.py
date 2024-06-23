"""
Contains all restrictions.
"""

from .disable_ability import DisableAbility
from .disable_ultimate import DisableUltimate
from .disable_summoner_spell import DisableSummonerSpell
from .disable_trinket import DisableTrinket
from .disable_Recall import DisableRecall
from .disable_on_dmg_taken import DisableOnDmgTaken
from .disable_on_resource_spend import DisableOnResourceSpend
from .disable_below_resource_value import DisableBelowResourceValue
from .disable_random_ability import DisableRandomAbility
from .switch_abilities import SwitchAbilities
from .auto_level import AutoLevel
from .auto_ability import AutoAbility
from .auto_summoner_spell import AutoSummonerSpell
from .auto_trinket import AutoTrinket
from .auto_recall import AutoRecall
from .auto_all_abilities import AutoAllAbilities
from .auto_move_buy import AutoMoveBuy
from .stop_move import StopMove
from .auto_chat import AutoChat
from .cover_map import CoverMap
from .lock_cam import LockCam
from .lock_ally_cam import LockAllyCam


all_restrictions = [
    # easy
    DisableAbility,
    DisableTrinket,
    AutoRecall,
    LockCam,
    StopMove,
    # mid
    DisableRecall,
    DisableUltimate,
    DisableSummonerSpell,
    AutoSummonerSpell,
    AutoTrinket,
    AutoLevel,
    SwitchAbilities,
    # hard
    DisableOnDmgTaken,
    DisableOnResourceSpend,
    DisableRandomAbility,
    AutoMoveBuy,
    AutoAbility,
    AutoAllAbilities,
    AutoChat,
    CoverMap,
    LockAllyCam,
    # alternating
    DisableBelowResourceValue,
]
