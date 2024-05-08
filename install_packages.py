import subprocess


def install_packages():
    try:
        subprocess.check_call(["pip", "install", "-r", "lol_quest/requirements.txt"])
    except subprocess.CalledProcessError as e:
        print("Fehler beim Installieren der Abhängigkeiten:", e)
