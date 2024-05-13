import os
import subprocess
import pkg_resources
import time


class PackageInstaller:

    @classmethod
    def start(cls):
        requirements_file_path = (
            os.path.dirname(os.path.abspath(__file__)) + "/requirements.txt"
        )
        missing_packages = cls.get_missing_packages(requirements_file_path)
        print(missing_packages)

        if any(missing_packages):
            cls.ask_for_consent(missing_packages)
        else:
            time.sleep(50)
            with open("installation_successful.txt", "w") as _:
                pass

    @classmethod
    def ask_for_consent(cls, missing_packages):
        os.system("cls")
        while True:
            replie = input(
                f"Install 0/{len(missing_packages)} requirements? (yes/no): "
            )
            if replie.lower() == "yes":
                cls.install_packages(missing_packages)
                with open("installation_successful.txt", "w") as _:
                    pass
                break
            elif replie.lower() == "no":
                break
            else:
                print("Input Error, write 'yes' or 'no'")

    @classmethod
    def get_missing_packages(cls, requirements_file):
        with open(requirements_file, "r", encoding="utf-16") as file:
            required_packages = [line.strip().casefold() for line in file.readlines()]
            print(required_packages)

        missing_packages = []
        installed_packages = [
            pkg.key + "==" + pkg.version for pkg in pkg_resources.working_set
        ]
        print(installed_packages)

        for package in required_packages:
            if package not in installed_packages:
                missing_packages.append(package)

        return missing_packages

    @classmethod
    def install_packages(cls, missing_packages):
        missing_packages_num = 0
        for package in missing_packages:
            os.system("cls")
            print(
                f"Installed {missing_packages_num}/{len(missing_packages)} requirements"
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
            missing_packages_num += 1

        print()
        print("Installation complete")
        time.sleep(2)


if __name__ == "__main__":
    PackageInstaller.start()
