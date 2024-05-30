from enum import Enum


class Constants(Enum):
    # hotkeys
    ABILITY = "ability"
    QUICK_ABILITY = "quick_ability"
    LEVEL_ABILITY = "level_ability"
    SUMMONER_SPELL = "summoner_spell"
    QUICK_SUMMONER_SPELL = "quick_summoner_spell"
    TRINKET = "trinket"
    TELEPORT = "teleport"
    SELECT_ALLY = "select_ally"
    SNAP_CAM = "snap_cam"
    STOP_POSITION = "stop_position"

    # events
    ENABLE = "enable"
    PRESS = "press"
    REMAP = "remap"
    PRESS_RELEASE = "press_release"

    # overlay
    MAP = "map"
    RESOURCE = "resource"

    # settings
    FLIP_MAP = "flip_map"
    MAP_SCALE = "map_scale"
    GLOBAL_SCALE = "global_scale"
    WINDOW_MODE = "window_mode"
    WIDTH = "width"
    HEIGHT = "height"
