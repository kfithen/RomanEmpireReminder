# RomanEmpireReminder

## Description

A simple Python script to remind the user of the Roman Empire at random intervals, all via toast notifications. The intervals range anywhere from every 5 minutes up to an hour.

> [!WARNING]
> I do not own any of the materials that are referenced or shared in this project. These images, sound effects, and other materials belong to their respective copyright holders. Please, do not sue me over some silly Python app!

## Why?

I made this project after remembering an old meme circling the internet in late 2023 where women would approach men and ask them how often they think about the Roman Empire. The meme was that if you were a man and didn't think of the Empire often enough, you would be considered feminine. Dumb, I know, but it spawned this beautiful program to remind you constantly so you don't end up too girly!

## Regarding PascalCase

This was originally written in C#, but I had such a hard time getting Microsoft's own libraries to work with Visual Studio that I decided to rewrite it in Python. Somehow, Python was much easier than using Microsoft's own tools (makes sense, right?), but I liked using C# so much that I wrote the Python script similarly to how I wrote the original script. So there you go, deal with it.

## Requirements

To install the requirements, just change your directory to the repository by using the ```cd``` command, then type the command ```pip install -r Requirements.txt``` afterward.

If for some reason that doesn't work, here is the list of requirements that the script uses:

```
datetime
pygame
pyttsx3
windows_toasts # Windows
dbus-python # Linux
```

The rest of the libraries required should be built into Python, but if not, please check the imports at the top of the Main.py file.

## How to Run

Change your directory to the repository by using the ```cd``` command, then run the command ```python Main.py```. That's it, now prepare to be reminded of the glorius Roman Empire!

## Contributing

Contributions are welcome as long as you don't try to make any drastic changes. As long as you do that, then I would be happy to look at any pull request and see if I approve!