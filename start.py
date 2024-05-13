import subprocess
import ctypes


def is_window_open(window_title):
    hwnd = ctypes.windll.user32.FindWindowW(None, window_title)
    return hwnd == 0


def main():
    window_title = "League of Quests"
    batch_file = "run.bat"

    if is_window_open(window_title):

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.Popen([batch_file], startupinfo=startupinfo)


if __name__ == "__main__":
    main()
