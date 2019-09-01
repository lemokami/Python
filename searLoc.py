import webbrowser as wb
import sys


args = sys.argv

if(len(args)>1):
    place = ''.join(args[1:])
    wb.open("https://www.google.com/maps/place/"+place)
else:
    place = input("Enter the place to be located:")
    wb.open("https://www.google.com/maps/place/"+place)


