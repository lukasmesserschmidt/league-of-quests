import re


# Mapping from LoL key names to keyboard library names
KEY_MAPPING = {
    # Special keys
    "Esc": "esc",
    "Space": "space",
    "Tab": "tab",
    "Return": "enter",
    "Enter": "enter",
    "Backspace": "backspace",
    "Delete": "delete",
    "Insert": "insert",
    "Home": "home",
    "End": "end",
    "Page Up": "page up",
    "Page Down": "page down",
    # Arrow keys
    "Up Arrow": "up",
    "Down Arrow": "down",
    "Left Arrow": "left",
    "Right Arrow": "right",
    # Function keys
    "F1": "f1",
    "F2": "f2",
    "F3": "f3",
    "F4": "f4",
    "F5": "f5",
    "F6": "f6",
    "F7": "f7",
    "F8": "f8",
    "F9": "f9",
    "F10": "f10",
    "F11": "f11",
    "F12": "f12",
    # Modifiers (these are handled separately)
    "Shift": "shift",
    "Ctrl": "ctrl",
    "Alt": "alt",
    "L Shift": "shift",
    "R Shift": "shift",
    "L Ctrl": "ctrl",
    "R Ctrl": "ctrl",
    "L Alt": "alt",
    "R Alt": "alt",
}


def parse_hotkey(hotkey_string: str) -> list[str]:
    if not hotkey_string or hotkey_string.strip() == "":
        return []

    # Split by comma for multiple bindings
    bindings = hotkey_string.split(",")
    result = []

    for binding in bindings:
        binding = binding.strip()

        # Check for unbound
        if "<Unbound>" in binding:
            continue

        # Extract all keys in brackets
        key_pattern = r"\[([^\]]+)\]"
        matches = re.findall(key_pattern, binding)

        if not matches:
            continue

        # Separate modifiers from the main key
        modifiers = []
        main_key = None

        for key in matches:
            key = key.strip()

            # Skip mouse buttons
            if key.startswith("Button"):
                main_key = None
                break

            # Check if it's a modifier
            if key in [
                "Shift",
                "Ctrl",
                "Alt",
                "L Shift",
                "R Shift",
                "L Ctrl",
                "R Ctrl",
                "L Alt",
                "R Alt",
            ]:
                mapped_modifier = KEY_MAPPING.get(key, key.lower())
                if mapped_modifier not in modifiers:
                    modifiers.append(mapped_modifier)
            else:
                # This is the main key
                main_key = key

        if main_key is None:
            continue

        # Map the main key
        mapped_main_key = KEY_MAPPING.get(main_key, main_key.lower())

        # Combine modifiers and main key
        if modifiers:
            result.append("+".join(modifiers) + "+" + mapped_main_key)
        else:
            result.append(mapped_main_key)

    return result
