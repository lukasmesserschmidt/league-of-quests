from PySide6.QtCore import QTimer
import threading
import requests
import warnings


class LiveClientData:
    all_data = None
    update_data = True
    url = "https://127.0.0.1:2999/liveclientdata/allgamedata"

    @classmethod
    def start_data_updater(cls):
        cls.request_data()

        cls.data_update_timer = QTimer()
        cls.data_update_timer.timeout.connect(cls.set_update_data)
        cls.data_update_timer.start(100)

        cls.import_loop_thread = threading.Thread(target=cls.request_data1, daemon=True)
        cls.import_loop_thread.start()

    @classmethod
    def set_update_data(cls):
        cls.update_data = True

    @classmethod
    def request_data(cls):
        return cls.all_data

    @classmethod
    def request_data1(cls):
        while True:
            # if cls.update_data:

            warnings.simplefilter("ignore")

            try:
                response = requests.get(cls.url, verify=False)
                cls.all_data = response.json()
            # cls.update_data = False
            except requests.exceptions.RequestException as e:
                pass
                # print(e)

            # return cls.all_data
