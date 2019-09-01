import re
import pyperclip 

text = pyperclip.paste()

phregex = re.compile(r'[a-zA-Z0-9._+]+\@+\w+\.+\w+\.*\w*')

lst = phregex.findall(text)

ntext = '\n'.join(lst)

pyperclip.copy(ntext)