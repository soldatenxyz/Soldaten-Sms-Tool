@echo off
title SOLDATEN SMS BOMBER
cd /d "%~dp0"

:: Python kontrol
python --version >nul 2>&1
if errorlevel 1 (
    echo [HATA] Python bulunamadi. Lutfen python.org'dan Python 3.8+ yukleyin.
    pause
    exit /b 1
)

:: Paket kontrol ve kur
echo [*] Bagimliliklar kontrol ediliyor...
python -m pip install aiohttp colorama --quiet --disable-pip-version-check

:: Calistir
echo [*] Baslatiliyor...
python main.py

:: Hata varsa terminal kapanmasin
if errorlevel 1 (
    echo.
    echo [HATA] Program bir hatayla kapandi. Yukaridaki mesaji inceleyin.
    pause
)
