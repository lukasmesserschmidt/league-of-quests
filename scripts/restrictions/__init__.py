from .disable_ability import DisableAbility
from .disable_ultimate import DisableUltimate
from .disable_summoner_spell import DisableSummonerSpell
from .disable_trinket import DisableTrinket
from .disable_Recall import DisableRecall
from .disable_on_dmg_taken import DisableOnDmgTaken
from .switch_abilities import SwitchAbilities
from .auto_level import AutoLevel
from .auto_ability import AutoAbility
from .auto_summoner_spell import AutoSummonerSpell
from .auto_move import AutoMove
from .stop_move import StopMove
from .cover_map import CoverMap
from .lock_cam import LockCam
from .lock_ally_cam import LockAllyCam


all_restrictions = [
    # easy
    DisableAbility,
    DisableTrinket,
    DisableRecall,
    LockCam,
    StopMove,
    # mid
    DisableUltimate,
    DisableSummonerSpell,
    AutoSummonerSpell,
    AutoLevel,
    AutoMove,
    SwitchAbilities,
    # hard
    DisableOnDmgTaken,
    AutoAbility,
    CoverMap,
    LockAllyCam,
]
