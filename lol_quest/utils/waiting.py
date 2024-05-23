import time


class WaitInterval:
    terminate_flag: bool
    interval: float | int

    @classmethod
    def wait_interval(cls):
        end_time = time.time() + cls.interval

        while time.time() < end_time and not cls.terminate_flag:
            time.sleep(0.01)
