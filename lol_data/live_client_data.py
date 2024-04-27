from contextlib import suppress
import threading
import requests
import warnings
import time


class LiveClientData:
    all_data = None
    url = "https://127.0.0.1:2999/liveclientdata/allgamedata"

    @classmethod
    def start(cls):
        cls.get_data()

        cls.import_loop_thread = threading.Thread(target=cls.request_data, daemon=True)
        cls.import_loop_thread.start()

    @classmethod
    def get_data(cls):
        return cls.all_data

    @classmethod
    def request_data(cls):
        while True:
            warnings.simplefilter("ignore")

            with suppress(Exception):
                response = requests.get(cls.url, verify=False)
                cls.all_data = response.json()

            time.sleep(0.2)
