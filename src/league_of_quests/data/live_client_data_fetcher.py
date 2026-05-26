import logging
import warnings

import requests


class LiveClientDataFetcher:
    def __init__(self):
        self.url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
        self.timeout = 5.0
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)

    def fetch(self) -> dict | None:
        try:
            warnings.simplefilter(
                "ignore",
                category=requests.packages.urllib3.exceptions.InsecureRequestWarning,
            )

            resp = self.session.get(self.url, verify=False, timeout=self.timeout)
            resp.raise_for_status()
            return resp.json()
        except requests.HTTPError as exc:
            self.logger.warning("Error fetching data from %s: %s", self.url, exc)
            return None
        except requests.exceptions.JSONDecodeError as exc:
            # JSON decode error
            self.logger.error("Invalid JSON received from %s: %s", self.url, exc)
            return None
