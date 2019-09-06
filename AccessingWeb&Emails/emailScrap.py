#simple program to take emails from copied text
import re #for regular expression
import pyperclip #pyperclip to access the clipboard(third party should be installed before running the program) 

text = pyperclip.paste() #.paste() -> taking the value from clipboard and pasting it here

phregex = re.compile(r'[a-zA-Z0-9._+]+\@+\w+\.+\w+\.*\w*') #uses regular expressions for checking the emails

lst = phregex.findall(text) #.findall looks for all email instances anf returns the list

ntext = '\n'.join(lst) #joining all the list elements and storing as a string

pyperclip.copy(ntext) #copying the string ntext to the clipboard of the user 

#After running the program paste the text in clipboard to find the result
