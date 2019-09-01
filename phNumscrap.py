import re
import pyperclip 

testtext = pyperclip.paste()

phregex = re.compile(r'\d{10}')

numlst = phregex.findall(testtext)

numbers = '\n'.join(numlst)

pyperclip.copy(numbers)