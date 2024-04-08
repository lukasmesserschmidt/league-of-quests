import requests
import warnings
import threading
import time


class LolData:
    all_data: dict

    @classmethod
    def init(cls):
        get_data = threading.Thread(target=cls.get_data, daemon=True)
        get_data.start()
        time.sleep(0.1)

    @classmethod
    def get_data(cls):
        while True:
            url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
            warnings.simplefilter("ignore")

            try:
                response = requests.get(url, verify=False)
                cls.all_data = response.json()
            except requests.exceptions.RequestException as e:
                print(e)

            # time.sleep(0.1)

    @classmethod
    def get_activePlayer_data(cls, key: str):
        return cls.all_data["activePlayer"][key]
