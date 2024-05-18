from .disable_ability import DisableAbility
from .disable_ultimate import DisableUltimate
from .disable_summoner_spell import DisableSummonerSpell
from .disable_trinket import DisableTrinket
from .disable_teleport import DisableTeleport
from .disable_on_dmg_taken import DisableOnDmgTaken
from .switch_abilities import SwitchAbilities
from .auto_level import AutoLevel
from .auto_ability import AutoAbility
from .auto_summoner_spell import AutoSummonerSpell
from .auto_move import AutoMove
from .cover_map import CoverMap
from .lock_cam import LockCam


all_restrictions = [
    # easy
    DisableAbility,
    DisableTrinket,
    DisableTeleport,
    LockCam,
    # mid
    DisableUltimate,
    DisableSummonerSpell,
    AutoSummonerSpell,
    AutoLevel,
    AutoMove,
    # hard
    DisableOnDmgTaken,
    AutoAbility,
    SwitchAbilities,
    CoverMap,
]
