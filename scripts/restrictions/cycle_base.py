"""
Aditional base class for cycling restrictions.
"""

import time


class CycleBase:
    """
    Adds a cycle interface to a restriction.
    """

    # init variables
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
            cls.condition_met()
            cls.cycle_end_time = time.time() + cls.cycle_duration
            cls.start_cycle = True

    @classmethod
    def start_condition(cls):
        """
        Checks if the start condition is met.
        """
        raise NotImplementedError

    @classmethod
    def condition_met(cls):
        """
        Everything that happens when the start condition is met.
        """

    @classmethod
    def cycle_content(cls):
        """
        Everything that happens during the cycle.
        """
        raise NotImplementedError

    @classmethod
    def cycle_end(cls):
        """
        Everything that happens when the cycle ends.
        """
