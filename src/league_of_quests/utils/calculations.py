def interpolate(min_val: float, max_val: float, ratio: float) -> float:
    """
    Interpolate between min_val and max_val based on ratio.
    ratio: 0.0 returns min_val, 1.0 returns max_val
    """
    return (min_val * (1 - ratio)) + (max_val * ratio)


def map_value(
    value: float, min_from: float, max_from: float, min_to: float, max_to: float
) -> float:
    """
    Map a value from range (min_from, max_from) to range (min_to, max_to).
    """
    return min_to + (value - min_from) * (max_to - min_to) / (max_from - min_from)
