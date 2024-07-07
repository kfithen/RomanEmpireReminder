# RomanEmpireReminder (Linux fork)
> [!WARNING]
> This is a fork of the original project that intends to reach compatibility with Linux through the use of `org.freedesktop.notification`

## Description

A simple Python script to remind the user of the Roman Empire at random intervals, via desktop notifications (notably, this fork aims to support Windows and most Linux platforms). The intervals range anywhere from every 5 minutes up to an hour. 

> [!WARNING]
> I do not own any of the materials that are referenced or shared in this project. These images, sound effects, and other materials belong to their respective copyright holders. Please, do not sue me over some silly Python app!

## Why?

- Talk about the old meme

## Regarding PascalCase

This was originally written in C#, but I had such a hard time getting Microsoft's own libraries to work with Visual Studio that I decided to rewrite it in Python. Somehow, Python was much easier than using Microsoft's own tools (makes sense, right?), but I liked using C# so much that I wrote the Python script similarly to how I wrote the original script. So there you go, deal with it.

## Requirements

To install the requirements, just change your directory to the repository and type the command ```pip install -r Requirements.txt```.

If for some reason that doesn't work, here is the list of requirements that the script uses:

```
datetime
pygame
pyttsx3
windows_toasts
```

You can also find the names of the required packages by simply looking at the imports at the top of the Python script.
