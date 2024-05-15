import os
import subprocess
import ctypes
import time


def is_window_open():
    window_title = "Setup League of Quests"
    class_name = "CASCADIA_HOSTING_WINDOW_CLASS"
    hwnd = ctypes.windll.user32.FindWindowW(class_name, window_title)

    return hwnd != 0


def get_path(path: str):
    path = os.path.dirname(os.path.abspath(__file__)) + path

    return path


def remove_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)


def reset_temp():
    create_shortcut_consent_path = get_path("\\temp\\create_shortcut_consent.txt")
    remove_file(installation_complete_path)
    remove_file(create_shortcut_consent_path)


def path_exists(path: str):
    if os.path.exists(path):
        return True


def execute_command(command: str):
    subprocess.Popen(command, shell=True)


def main():
    global installation_complete_path

    sleep_duration = 0.2
    venv_path = get_path("\\.venv\\Scripts\\python.exe")
    run_bat_path = get_path("\\setup.bat")
    installation_complete_path = get_path("\\temp\\installation_complete.txt")
    main_path = get_path("\\main.py")
    setup_command = f'start cmd.exe /c "{run_bat_path}"'
    main_command = f'"{venv_path}" "{main_path}"'

    reset_temp()

    execute_command(setup_command)

    while not is_window_open() and not path_exists(installation_complete_path):
        time.sleep(sleep_duration)
    while is_window_open():
        time.sleep(sleep_duration)

    if path_exists(installation_complete_path):
        execute_command(main_command)

    reset_temp()
