#!/bin/bash
# SOLDATEN SMS BOMBER - Kali Linux starter

cd "$(dirname "$0")"

# Python kontrol
if ! command -v python3 &>/dev/null; then
    echo "[HATA] python3 bulunamadi. 'sudo apt install python3' ile yukleyin."
    exit 1
fi

# Paketleri kur
echo "[*] Bagimliliklar kontrol ediliyor..."
python3 -m pip install aiohttp colorama --quiet --break-system-packages 2>/dev/null || \
python3 -m pip install aiohttp colorama --quiet

# Calistir
python3 main.py
