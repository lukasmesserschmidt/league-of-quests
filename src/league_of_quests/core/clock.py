from .states import ClockState


class Clock:
    def __init__(self, duration: float):
        self._duration = duration
        self._time_left = duration
        self._state = ClockState.INACTIVE

        self._use_holding = False
        self._holding_duration = 0.0
        self._holding_time_left = 0.0

    def configure_holding(self, enabled: bool, duration: float = 0.0):
        self._use_holding = enabled
        self._holding_duration = duration
        self._holding_time_left = duration

    def is_holding(self):
        return self._state == ClockState.HOLDING

    def get_state(self):
        return self._state

    def set_state(self, state: ClockState):
        self._state = state

    def get_time_left(self):
        return self._time_left

    def get_holding_time_left(self):
        return self._holding_time_left

    def update(self, dt: float):
        # reduce the remaining time
        match self._state:
            case ClockState.ACTIVE:
                if self._time_left > 0:
                    self._time_left -= dt
                else:
                    self.set_state(ClockState.TIMER_EXPIRED)

            case ClockState.HOLDING:
                # currently in holding state, check if holding time has elapsed
                if self._holding_time_left > 0:
                    self._holding_time_left -= dt
                else:
                    # holding time completed, mark quest as completed
                    self.set_state(ClockState.TIMER_EXPIRED)
            case ClockState.TIMER_EXPIRED:
                # timer expired, do nothing
                pass

    def reset(self):
        self._time_left = self._duration
        self._holding_time_left = self._holding_duration
        self.set_state(ClockState.ACTIVE)

    def activate_holding(self):
        self.set_state(ClockState.HOLDING)
        self._holding_time_left = self._holding_duration

    def deactivate_holding(self):
        self.set_state(ClockState.ACTIVE)
        self._holding_time_left = 0.0
