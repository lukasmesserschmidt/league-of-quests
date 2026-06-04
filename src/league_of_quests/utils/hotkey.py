import re
import keyboard


def parse_hotkey(hotkey_string: str) -> list[str]:
    if not hotkey_string or hotkey_string.strip() == "":
        return []

    # Extract all keys in brackets
    key_pattern = r"\[([^\]]+)\]"
    matches = re.findall(key_pattern, hotkey_string)

    result = []

    for key in matches:
        key = key.strip()

        # Check if key is valid using keyboard library
        scan_codes = keyboard.key_to_scan_codes(key, False)
        if not scan_codes:
            continue

        # Normalize key name using keyboard library
        normalized_key = keyboard.get_hotkey_name((key,))

        # Add to result if not already present
        if normalized_key not in result:
            result.append(normalized_key)

    return result
