import os
import win32com.client
import time


class CreateShortcut:
    exe_path = (
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        + "/League of Quests.exe"
    )
    shortcut_name = "League of Quests"
    icon_path = (
        os.path.dirname(os.path.abspath(__file__)) + "/lol_quest/graphics/loq_icon.ico"
    )

    @classmethod
    def start(cls):
        if not os.path.exists(cls.get_shortcut_path()):
            cls.ask_for_consent()

    @classmethod
    def ask_for_consent(cls):
        os.system("cls")

        while True:
            replie = input("Create desktop shortcut? (yes/no): ")

            if replie.lower() == "yes":
                cls.create_desktop_shortcut(cls.exe_path, cls.icon_path)

                print()
                print("Desktop shortcut created")
                time.sleep(1)
                break
            elif replie.lower() == "no":
                break
            else:
                print("Input Error, write 'yes' or 'no'")

    @classmethod
    def create_desktop_shortcut(cls, target_path, icon_path=None):
        shortcut_path = cls.get_shortcut_path()

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = target_path
        if icon_path:
            shortcut.IconLocation = icon_path
        shortcut.Save()

    @classmethod
    def get_shortcut_path(cls):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        shortcut_path = os.path.join(desktop_path, cls.shortcut_name + ".lnk")

        return shortcut_path


if __name__ == "__main__":
    CreateShortcut.start()
