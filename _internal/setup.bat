@echo off

title Setup League of Quests

set "batch_path=%~dp0"
set "venv_path=%batch_path%\.venv\Scripts\python.exe"
set "temp_path=%batch_path%\temp"

if not exist "%temp_path%" (
    mkdir "%temp_path%"
)

"%venv_path%" "%batch_path%\package_installer.py"

if exist "%temp_path%\create_shortcut_consent.txt" (
del "%temp_path%\create_shortcut_consent.txt"

"%venv_path%" "%batch_path%\create_shortcut.py"
)
