import requests
import warnings
import threading
import time


class LolData:
    all_data: dict

    @classmethod
    def get_data(cls):
        cls.terminate_flag = False
        request_data = threading.Thread(target=cls.request_data, daemon=True)
        request_data.start()

    @classmethod
    def request_data(cls):
        while True:
            url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
            warnings.simplefilter("ignore")

            try:
                response = requests.get(url, verify=False)
                cls.all_data = response.json()
            except requests.exceptions.RequestException as e:
                print(e)

            if cls.terminate_flag:
                break

            # time.sleep(0.1)

    @classmethod
    def get_activePlayer_data(cls, key: str):
        return cls.all_data["activePlayer"][key]
