def convert_hotkey(hotkey: str):
    hotkey = hotkey.replace("[", "").split("]")
    while "" in hotkey:
        hotkey.remove("")
    hotkey = "+".join(hotkey)

    return hotkey
