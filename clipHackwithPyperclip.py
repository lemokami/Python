#you should install pyperclip using pip-install at first to run the program

import pyperclip 
#pyperclip is a thirdparty python library, it contains copy() and paste() for copying to the clipboard and pasting it

name = input("Enter your name:")

pyperclip.copy(f"My name is {name}")

print("See your clipboard for seeing  pyperclip's magic")