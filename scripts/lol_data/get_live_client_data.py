"""
This module contains the GetLiveClientData class.
"""

import time
import warnings

from contextlib import suppress
import threading
import requests


class GetLiveClientData:
    """
    This class requests the live client data.
    """

    # init variables
    all_data = {}
    _url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
    _request_loop_thread = None

    _terminate_flag = False

    @classmethod
    def start(cls):
        """
        Starts the import loop.
        """
        if cls._request_loop_thread is None:
            cls._terminate_flag = False
            cls._request_loop_thread = threading.Thread(
                target=cls._request_data, daemon=True
            )

        cls._request_loop_thread.start()

    @classmethod
    def stop(cls):
        """
        Stops the import loop.
        """
        if cls._request_loop_thread is not None:
            cls._terminate_flag = True
            cls._request_loop_thread.join()

    @classmethod
    def _request_data(cls):
        while not cls._terminate_flag:
            warnings.simplefilter("ignore")

            with suppress(Exception):
                response = requests.get(cls._url, verify=False, timeout=1)
                all_data = response.json()
                if len(all_data["events"]["Events"]) > 0:
                    cls.all_data = all_data

            time.sleep(0.5)
