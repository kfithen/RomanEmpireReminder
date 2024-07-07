#    ___                         ____           _           ___            _         __       
#   / _ \___  __ _  ___ ____    / __/_ _  ___  (_)______   / _ \___ __ _  (_)__  ___/ /__ ____
#  / , _/ _ \/  ' \/ _ `/ _ \  / _//  ' \/ _ \/ / __/ -_) / , _/ -_)  ' \/ / _ \/ _  / -_) __/
# /_/|_|\___/_/_/_/\_,_/_//_/ /___/_/_/_/ .__/_/_/  \__/ /_/|_|\__/_/_/_/_/_//_/\_,_/\__/_/   
#                                      /_/                                                     
#
# Version: ?
# Last Updated: 7/3/2024
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

        self.NotificationArray = [
            {
                "Image": "Image/Buddy_Christ.jpg", 
                "Heading": "Buddy Christ",
                "Body": "I just got hung on a cross for being too popular, only to become even more popular!", 
                "Audio": "Audio/Got_Em.mp3"
            },
            {
                "Image": "Image/Julius_Caesar_Getting_Stabbed.jpg", 
                "Heading": "Julius Caesar", 
                "Body": "Beware the Ides of March? Nah bruh, blud is yappin fr fr.",
                "Audio": "Audio/What_Is_Blud_Yapping_About.mp3"
            },
            {
                "Image": "Image/Marcus_Aurelius.jpg", 
                "Heading": "Marcus Aurelius", 
                "Body": "IHATEMYLIFEIHATEMYLIFEIHATEMYLIFEIHATEMYLIFEIHATEMYLIFE",
                "Audio": "Audio/Man_Screaming.mp3"
            },
            {
                "Image": "Image/Ok_Sure_Bill_Wurtz.png", 
                "Heading": "Bill Wurtz", 
                "Body": '"Is loving Jesus legal yet? Uh, no. Wait, actually, sure." - Constantine',
                "Audio": "Audio/Is_Loving_Jesus_Legal_Yet.mp3"
            },
            {
                "Image": "Image/They_Split.png",
                "Heading": "The Roman Empire",
                "Body": "Our nation is the greatest nation! It will never spl-",
                "Audio": "Audio/Oops.mp3"
            },
            {
                "Image": "Image/Stoicism.png", 
                "Heading": "Stoicism", 
                "Body": '"Life is hard, L, deal with it."',
                "Audio": "Audio/Baby_Crying.mp3"
            }
        ]

    def SetConsole(self) -> None:
        os.system("cls")
        os.system("title Roman Empire Reminder")

    def PrintHeader(self) -> None:
        print(r"""   
           ___                         ____           _           ___            _         __       
          / _ \___  __ _  ___ ____    / __/_ _  ___  (_)______   / _ \___ __ _  (_)__  ___/ /__ ____
         / , _/ _ \/  ' \/ _ `/ _ \  / _//  ' \/ _ \/ / __/ -_) / , _/ -_)  ' \/ / _ \/ _  / -_) __/
        /_/|_|\___/_/_/_/\_,_/_//_/ /___/_/_/_/ .__/_/_/  \__/ /_/|_|\__/_/_/_/_/_//_/\_,_/\__/_/   
                                             /_/                                                    
        """)
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
