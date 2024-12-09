import time
import random

from RomanEmpireReminder import RomanEmpireReminder

Program = RomanEmpireReminder()
Program.SetConsole()
Program.PrintHeader()
Program.CheckOperatingSystem()

while True:
    try:
        Interval = random.randint(300, 3600)
        time.sleep(Interval)
        Program.RemindOfRomanEmpire()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Exiting...\n")
        time.sleep(1)
        exit()
