#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════╗
║     SOLDATEN SMS BOMBER  -  main.py      ║
║     Python 3.8+  |  Kali Linux Ready     ║
╚══════════════════════════════════════════╝
"""

import asyncio
import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

# ─── Modülleri içe aktar ───────────────────────────────────────────────────────
from modules.ascii_art   import print_banner, print_stats
from modules.animations  import loading_animation, matrix_rain, countdown
from modules.sms         import sms_bomber


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def separator(color=Fore.YELLOW):
    print(color + "━" * 72 + Style.RESET_ALL)


def prompt(label: str, color=Fore.RED) -> str:
    return input(color + Style.BRIGHT + label + Style.RESET_ALL + Fore.WHITE + " " + Style.RESET_ALL)


async def main():
    # ── Banner ──────────────────────────────────────────────────────────────
    print_banner()

    # ── Loading animasyonları ────────────────────────────────────────────────
    loading_animation("Initializing kernel modules",          1.5)
    loading_animation("Loading target acquisition systems",   1.2)
    loading_animation("Connecting to anonymous networks",     1.5)
    loading_animation("Activating payload vectors",           1.0)

    print(Fore.RED + "\n[SYSTEM] All systems operational. Ready for mission.\n" + Style.RESET_ALL)

    # ── Hedef telefon numarası ───────────────────────────────────────────────
    separator()
    telefon = prompt("[TARGET] Enter phone number (10 digits, without +90): ").strip()

    if len(telefon) != 10 or not telefon.isdigit():
        print(Fore.RED + "❌ [ERROR] Phone number must be exactly 10 digits. Ex: 5401234521" + Style.RESET_ALL)
        sys.exit(1)

    # ── Bomba miktarı ────────────────────────────────────────────────────────
    separator()
    miktar_str = prompt("[PAYLOAD] How many rounds to deploy (each round = 50 services): ").strip()

    if not miktar_str.isdigit() or int(miktar_str) == 0:
        print(Fore.RED + "❌ [ERROR] Please enter a valid positive number." + Style.RESET_ALL)
        sys.exit(1)

    miktar = int(miktar_str)

    # ── İstatistik ekranı ────────────────────────────────────────────────────
    print_stats(telefon, miktar)

    # ── Geri sayım ───────────────────────────────────────────────────────────
    print(Fore.RED + Style.BRIGHT + "\n🚀 MISSION COUNTDOWN INITIATED..." + Style.RESET_ALL)
    countdown(5)

    # ── Matrix efekti ────────────────────────────────────────────────────────
    matrix_rain(2)

    print(Fore.GREEN + Style.BRIGHT + "\n🔥 MISSION STARTED - SMS BOMBING IN PROGRESS 🔥\n" + Style.RESET_ALL)

    # ── SMS Bomber'ı başlat ─────────────────────────────────────────────────
    await sms_bomber(telefon, miktar)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n⛔ [ABORT] Mission aborted by user." + Style.RESET_ALL)
        sys.exit(0)
