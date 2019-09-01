import webbrowser as wb
import sys

args = sys.argv

if(len(args)>1):
    search = ''.join(args[1:])
    wb.open("https://www.google.com/search?&q="+search)
else:
    search = input("Search on google:")
    wb.open("https://www.google.com/search?&q="+search)