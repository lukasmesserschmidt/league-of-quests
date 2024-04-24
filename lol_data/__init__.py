from .get_lol_settings import GetLolSettings
from .live_client_data import LiveClientData


LiveClientData.start_data_updater()
GetLolSettings.start()
