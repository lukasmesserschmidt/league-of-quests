import time

from .platform import KeyboardController


def main():
    keyboard_controller = KeyboardController()
    keyboard_controller.block_key("q")

    time.sleep(5)
    keyboard_controller.press_release_key("w")

    # time.sleep(20)


if __name__ == "__main__":
    main()
