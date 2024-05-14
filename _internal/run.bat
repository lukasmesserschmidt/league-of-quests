@echo off

if exist "create_shortcut_consent.txt" (
del "create_shortcut_consent.txt"
)
if exist "installation_successful.txt" (
del "installation_successful.txt"
)


set "batch_path=%~dp0"
set "venv_path=%batch_path%\.venv\Scripts\python.exe"

start /wait "Package Installer" "%venv_path%" "%batch_path%\package_installer.py"

if exist "create_shortcut_consent.txt" (
del "create_shortcut_consent.txt"

start /wait "Create Desktop Shortcut" "%venv_path%" "%batch_path%\create_shortcut.py"
)

if exist "installation_successful.txt" (
del "installation_successful.txt"

"%venv_path%" "%batch_path%\main.py"
)

