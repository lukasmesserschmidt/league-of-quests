from contextlib import suppress
import threading
import requests
import warnings

from ..utils.waiting import WaitInterval


class GetLiveClientData(WaitInterval):
    all_data = {}
    url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
    import_loop_thread = None

    terminate_flag = False
    interval = 0.2

    @classmethod
    def start(cls):
        if cls.import_loop_thread is None:
            cls.terminate_flag = False
            cls.import_loop_thread = threading.Thread(
                target=cls.request_data, daemon=True
            )

        cls.import_loop_thread.start()

    @classmethod
    def stop(cls):
        if cls.import_loop_thread is not None:
            cls.terminate_flag = True
            cls.import_loop_thread.join()

    @classmethod
    def request_data(cls):
        while not cls.terminate_flag:
            warnings.simplefilter("ignore")

            with suppress(Exception):
                response = requests.get(cls.url, verify=False)
                cls.all_data = response.json()

            cls.wait_interval()
