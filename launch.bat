@echo off

if Not Exist "%CD%\venv\" (
    py -m venv venv
    CALL %CD%\venv\Scripts\activate.bat
    py -m pip install -r %CD%\requirements.txt
) else (
    CALL %CD%\venv\Scripts\activate.bat
)

py bot.py
