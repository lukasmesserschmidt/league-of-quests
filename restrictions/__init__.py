from .disable_ability_0_3 import (
    DisableAbility0,
    DisableAbility1,
    DisableAbility2,
    DisableAbility3,
)
from .disable_summoner_spell_0_1 import DisableSummonerSpell0, DisableSummonerSpell1
from .disable_on_dmg_taken import DisableOnDmgTaken
from .auto_level import AutoLevel
from .auto_move import AutoMove
from .cover_map import CoverMap


all_restrictions = [
    DisableAbility0,
    DisableAbility1,
    DisableAbility2,
    DisableAbility3,
    DisableSummonerSpell0,
    DisableSummonerSpell1,
    DisableOnDmgTaken,
    AutoLevel,
    AutoMove,
    CoverMap,
]
