import time


class CycleBase:
    start_cycle = False
    cycle_end_time = 0
    cycle_duration = 0

    @classmethod
    def init(cls):
        cls.start_cycle = False
        cls.cycle_end_time = 0

    @classmethod
    def restriction_content(cls):
        if cls.start_cycle:
            if time.time() < cls.cycle_end_time:
                cls.cycle_content()
            else:
                cls.cycle_end()
                cls.start_cycle = False
        elif cls.start_condition():
            cls.cycle_end_time = time.time() + cls.cycle_duration
            cls.condition_met()
            cls.start_cycle = True

    @classmethod
    def start_condition(cls):
        raise NotImplementedError

    @classmethod
    def condition_met(cls):
        pass

    @classmethod
    def cycle_content(cls):
        raise NotImplementedError

    @classmethod
    def cycle_end(cls):
        pass
