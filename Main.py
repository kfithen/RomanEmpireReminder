#    ___                         ____           _           ___            _         __       
#   / _ \___  __ _  ___ ____    / __/_ _  ___  (_)______   / _ \___ __ _  (_)__  ___/ /__ ____
#  / , _/ _ \/  ' \/ _ `/ _ \  / _//  ' \/ _ \/ / __/ -_) / , _/ -_)  ' \/ / _ \/ _  / -_) __/
# /_/|_|\___/_/_/_/\_,_/_//_/ /___/_/_/_/ .__/_/_/  \__/ /_/|_|\__/_/_/_/_/_//_/\_,_/\__/_/   
#                                      /_/                                                     
#
# Version: ?
# Last Updated: 7/7/2024
# Creator & Maintainer: Kendrick Fithen

import datetime
import json
import os
import platform
from pygame import mixer
import pyttsx3
import random
import time
from windows_toasts import Toast, ToastDisplayImage, WindowsToaster

class RomanEmpireReminder:
    def __init__(self) -> None:
        self.NotificationIndex = 0
        self.NotificationArray = []

        with open('Config.json', 'r') as NotificationConfig:
            ConfigData = json.load(NotificationConfig)
            self.NotificationArray = ConfigData.get("NotificationArray", [])

    def SetConsole(self) -> None:
        os.system("cls")
        os.system("title Roman Empire Reminder")

    def PrintHeader(self) -> None:
        print("""   
           ___                         ____           _           ___            _         __       
          / _ \___  __ _  ___ ____    / __/_ _  ___  (_)______   / _ \___ __ _  (_)__  ___/ /__ ____
         / , _/ _ \/  ' \/ _ `/ _ \  / _//  ' \/ _ \/ / __/ -_) / , _/ -_)  ' \/ / _ \/ _  / -_) __/
        /_/|_|\___/_/_/_/\_,_/_//_/ /___/_/_/_/ .__/_/_/  \__/ /_/|_|\__/_/_/_/_/_//_/\_,_/\__/_/   
                                             /_/                                              \n""")
        print("Version: ?\nLast Updated: 7/3/2024\nCreator & Maintainer: Kendrick Fithen\n")

    def CheckOperatingSystem(self) -> None:
        if (platform.system() != "Windows" or platform.release() not in ["10", "11"]):
            print("You can't run this program on anything other than Windows 10 or 11. Sorry!")
            time.sleep(1)
            exit()
        
    def RandomizeIndex(self) -> None:
        self.NotificationIndex = random.randint(0, len(self.NotificationArray) - 1)

    def PrintReminder(self) -> None:
        CurrentDateTime = datetime.datetime.now()
        FormattedDateTime = CurrentDateTime.strftime("%m/%d/%y %H:%M:%S")
        print(FormattedDateTime + ": Reminded of the Roman Empire!")

    def PlayNotificationAudio(self) -> None:
        mixer.init()
        mixer.music.load(self.NotificationArray[self.NotificationIndex]["Audio"])
        mixer.music.play()

    def SayToastNotification(self) -> None:
        NotificationAudioLength = mixer.Sound(self.NotificationArray[self.NotificationIndex]["Audio"]).get_length()
        time.sleep(NotificationAudioLength)
        TextToSpeech = pyttsx3.init()
        TextToSpeech.say(self.NotificationArray[self.NotificationIndex]["Body"])
        TextToSpeech.runAndWait()

    def RemindOfRomanEmpire(self) -> None:
        self.RandomizeIndex()
        self.PrintReminder()
        Toaster = WindowsToaster("Python")
        ToastNotification = Toast()
        ToastNotification.AddImage(ToastDisplayImage.fromPath(self.NotificationArray[self.NotificationIndex]["Image"]))
        ToastNotification.text_fields = [
            self.NotificationArray[self.NotificationIndex]["Heading"],
            self.NotificationArray[self.NotificationIndex]["Body"]
        ]
        self.PlayNotificationAudio()
        Toaster.show_toast(ToastNotification)
        self.SayToastNotification()

if __name__ == "__main__":
    Program = RomanEmpireReminder()
    Program.SetConsole()
    Program.PrintHeader()
    Program.CheckOperatingSystem()
    
    while True:
        try:
            Program.RemindOfRomanEmpire()
            # Interval = random.randint(300, 3600)
            Interval = 30
            time.sleep(Interval)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: Exiting...\n")
            time.sleep(1)
            exit()