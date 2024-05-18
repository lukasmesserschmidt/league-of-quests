import os
from ..lol_data.get_lol_paths import get_lol_config_path


def is_lol_installed():
    try:
        return os.path.exists(get_lol_config_path())
    except:
        return False
