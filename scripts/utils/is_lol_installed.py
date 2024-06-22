"""
This module contains functions for checking if the League of Legends is installed.
"""

import os
from contextlib import suppress

from ..lol_data.get_lol_paths import get_lol_config_path


def is_lol_installed():
    """
    Returns if the League of Legends is installed.
    """
    with suppress(Exception):
        return os.path.exists(get_lol_config_path())
    return False
