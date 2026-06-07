#!/usr/bin/env python3
"""
Reanimal Memory Scanner – Find player health and position addresses.
Open source – no game memory modification.
"""

import pymem
import pymem.process
import time

def main():
    print("[INFO] Searching for Reanimal process...")
    try:
        pm = pymem.Pymem("Reanimal.exe")
        print("[SUCCESS] Process found!")
    except pymem.exception.ProcessNotFound:
        print("[ERROR] Game not running. Start Reanimal first.")
        return

    module = pymem.process.module_from_name(pm.process_handle, "Reanimal.exe")
    base = module.lpBaseOfDll
    print(f"[INFO] Base address: {hex(base)}")

    print("[INFO] This is a demo. The full trainer is in Releases.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()