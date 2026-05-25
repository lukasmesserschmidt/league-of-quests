import logging
from typing import Optional, Dict, Any
import warnings

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class LiveClientDataFetcher:
    """Fetch live client data with a reusable requests session.

    Features:
    - Reusable `requests.Session` for connection pooling
    """

    def __init__(self):
        self.url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
        self.verify = False
        self.timeout = 5.0
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)

    def fetch(self) -> Optional[Dict[str, Any]]:
        try:
            if not self.verify:
                warnings.simplefilter(
                    "ignore",
                    category=requests.packages.urllib3.exceptions.InsecureRequestWarning,
                )

            resp = self.session.get(self.url, verify=self.verify, timeout=self.timeout)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as exc:
            self.logger.warning("Error fetching data from %s: %s", self.url, exc)
            return None
        except ValueError as exc:
            # JSON decode error
            self.logger.error("Invalid JSON received from %s: %s", self.url, exc)
            return None
