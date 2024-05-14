import os
import subprocess
from importlib.metadata import distributions
import time


class PackageInstaller:

    @classmethod
    def start(cls):
        requirements_file_path = (
            os.path.dirname(os.path.abspath(__file__)) + "/requirements.txt"
        )
        missing_packages = cls.get_missing_packages(requirements_file_path)

        if any(missing_packages):
            cls.ask_for_consent(missing_packages)
            cls.create_shortcut_consent()
        else:
            cls.installation_successful()

    @classmethod
    def ask_for_consent(cls, missing_packages):
        os.system("cls")
        while True:
            replie = input(
                f"Install 0/{len(missing_packages)} requirements? (yes/no): "
            )

            if replie.lower() == "yes":
                cls.install_packages(missing_packages)
                cls.installation_successful()

                print()
                print("Installation complete")
                time.sleep(1)
                break
            elif replie.lower() == "no":
                break
            else:
                print("Input Error, write 'yes' or 'no'")

    @classmethod
    def installation_successful(cls):
        with open("installation_successful.txt", "w") as _:
            pass

    @classmethod
    def create_shortcut_consent(cls):
        with open("create_shortcut_consent.txt", "w") as _:
            pass

    @classmethod
    def get_missing_packages(cls, requirements_file):
        with open(requirements_file, "r", encoding="utf-16") as file:
            required_packages = [line.strip() for line in file.readlines()]

        missing_packages = []
        installed_packages = [
            package.metadata["Name"] + "==" + package.version
            for package in distributions()
        ]

        for package in required_packages:
            if package not in installed_packages:
                missing_packages.append(package)

        return missing_packages

    @classmethod
    def install_packages(cls, missing_packages):
        missing_packages_num = 0
        for package in missing_packages:
            missing_packages_num += 1

            os.system("cls")
            print(
                f"Installing requirement {missing_packages_num}/{len(missing_packages)}"
            )
            print()

            subprocess.check_call(
                [
                    "pip",
                    "install",
                    package,
                    "--upgrade",
                    "--target",
                    os.path.dirname(os.path.abspath(__file__))
                    + "/.venv/Lib/site-packages",
                ]
            )


if __name__ == "__main__":
    PackageInstaller.start()
