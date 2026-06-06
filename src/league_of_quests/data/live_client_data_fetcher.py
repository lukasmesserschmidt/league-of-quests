import warnings
from urllib3.exceptions import InsecureRequestWarning

import requests

from .models import LiveClientData


class LiveClientDataFetcher:
    def __init__(self):
        self.url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
        self.timeout = 5.0
        self.session = requests.Session()

        warnings.simplefilter("ignore", category=InsecureRequestWarning)

    def fetch(self) -> LiveClientData | None:
        try:
            resp = self.session.get(self.url, verify=False, timeout=self.timeout)
            resp.raise_for_status()
            json_data = resp.json()
            return LiveClientData(**json_data)
        except Exception:
            return None
