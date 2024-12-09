import time
import random
import importlib.resources

from . import RomanEmpireReminder

with importlib.resources.as_file(importlib.resources.files("roman-empire-reminder")) as path:
    Program = RomanEmpireReminder(path)
    Program.SetConsole()
    Program.PrintHeader()
    Program.CheckOperatingSystem()

    while True:
        try:
            Interval = 3#random.randint(300, 3600)
            time.sleep(Interval)
            Program.RemindOfRomanEmpire()
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: Exiting...\n")
            time.sleep(1)
            exit()
