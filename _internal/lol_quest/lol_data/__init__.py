from .get_lol_settings import GetLolSettings
from .get_live_client_data import GetLiveClientData
from .lol_window_data import LolWindowData
from ..utils.is_lol_installed import is_lol_installed

if is_lol_installed():
    GetLolSettings.start()
    GetLiveClientData.start()
    LolWindowData.start()
