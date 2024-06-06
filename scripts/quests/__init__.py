from .spend_gold_timer import SpendGoldTimer
from .get_kill_timer import GetKillTimer
from .have_low_gold import HaveLowGold
from .have_x_gold import HaveXGold
from .dont_spend_resources import DontSpendResources
from .dont_take_dmg import DontTakeDmg
from .get_cs import GetCs
from .get_ward_score import GetWardScore
from .get_x_stat import GetXStat
from .get_one_kill import GetOneKill
from .solo_kill import SoloKill
from .steal_kill import StealKill
from .help_get_kill import HelpGetKill
from .assist_objective import AssistObjective
from .kill_objective import KillOjective
from .dont_die import DontDie
from .buy_dark_seal import BuyDarkSeal
from .buy_health_potion import BuyHealthPotion


all_quests = [
    # easy
    HaveLowGold,
    GetCs,
    GetWardScore,
    GetXStat,
    DontTakeDmg,
    DontDie,
    # mid
    SpendGoldTimer,
    DontSpendResources,
    GetOneKill,
    HelpGetKill,
    AssistObjective,
    # hard
    HaveXGold,
    SoloKill,
    StealKill,
    KillOjective,
    GetKillTimer,
    BuyDarkSeal,
    # alternating
    BuyHealthPotion,
]
