"""
This module contains functions for converting time.
"""


def convert_time(seconds: float):
    """
    Converts seconds to minutes and seconds.
    """
    minutes = str(int(seconds // 60))
    seconds = str(int(seconds % 60))
    units = [minutes, seconds]
    for i in range(2):
        while len(units[i]) < 2:
            units[i] = "0" + units[i]

    text = f"{units[0]}:{units[1]}"

    return text
