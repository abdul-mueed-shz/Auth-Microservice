
:: Batch script to setup a virtual development environment

@echo off

:: Variables
set venv_folder=.\build-env

:: Creating virtual environment
echo Creating virtual environment
echo.

if exist %venv_folder%\ (
    echo Virtual environment already exists
    echo.
    goto activate
) else (
    python -m venv "%venv_folder%"
)

:: Activating virtual environment
:activate
echo Activating virtual environment
echo.

call %venv_folder%\Scripts\activate.bat

:: Update pip
echo Updating pip in virtual environment
echo.
python.exe -m pip install --upgrade pip

:end