@echo off
".venv\Scripts\python.exe" -m pip install setuptools

start /wait "installing requirements" ".venv\Scripts\python.exe" "install_packages.py"

if exist "installation_successful.txt" (
del "installation_successful.txt"

".venv\Scripts\python.exe" "main.py"
)