import os
import subprocess
from importlib.metadata import distributions
import time


class PackageInstaller:

    @classmethod
    def start(cls):
        requirements_file_path = cls.get_path("/requirements.txt")
        missing_packages = cls.get_missing_packages(requirements_file_path)

        if any(missing_packages):
            cls.ask_for_consent(missing_packages)
        else:
            cls.installation_complete()

    @classmethod
    def ask_for_consent(cls, missing_packages):
        os.system("cls")

        while True:
            replie = input(
                f"Install 0/{len(missing_packages)} requirements? (yes/no): "
            )

            if replie.lower() == "yes":
                cls.install_packages(missing_packages)
                cls.installation_complete()
                cls.create_shortcut_consent()

                print()
                print("Installation complete")
                time.sleep(1)
                break
            elif replie.lower() == "no":
                break
            else:
                print("Input Error, write 'yes' or 'no'")

    @classmethod
    def installation_complete(cls):
        cls.create_txt_file("\\installation_complete.txt")

    @classmethod
    def create_shortcut_consent(cls):
        cls.create_txt_file("\\create_shortcut_consent.txt")

    @classmethod
    def create_txt_file(cls, file_name: str):
        file_path = cls.get_path("\\temp" + file_name)

        with open(file_path, "w") as _:
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

            path = cls.get_path("\\.venv\\Lib\\site-packages")
            subprocess.check_call(
                [
                    "pip",
                    "install",
                    "--upgrade",
                    "--target",
                    path,
                    package,
                ]
            )

    @classmethod
    def get_path(cls, path: str):
        path = os.path.dirname(os.path.abspath(__file__)) + path

        return path


if __name__ == "__main__":
    PackageInstaller.start()
