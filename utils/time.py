def convert_time(seconds: float):
    min = str(int(seconds // 60))
    sec = str(int(seconds % 60))
    units = [min, sec]
    for i in range(2):
        while len(units[i]) < 2:
            units[i] = "0" + units[i]

    text = f"{units[0]}:{units[1]}"

    return text
