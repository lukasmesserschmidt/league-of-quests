from .have_low_gold import HaveLowGold
from .spend_gold_timer import SpendGoldTimer
from .have_x_gold import HaveXGold
from .dont_spend_resources import DontSpendResources
from .get_cs import GetCs
from .get_ward_score import GetWardScore
from .solo_kill import SoloKill
from .steal_kill import StealKill
from .help_get_kill import HelpGetKill
from .buy_dark_seal import BuyDarkSeal


all_quests = [
    # # easy
    # HaveLowGold,
    # GetCs,
    # GetWardScore,
    # # mid
    # SpendGoldTimer,
    # DontSpendResources,
    HelpGetKill,
    # # hard
    # HaveXGold,
    # SoloKill,
    # StealKill,
    # BuyDarkSeal,
]
