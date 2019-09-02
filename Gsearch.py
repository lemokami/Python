#a simple program to take a keyword as argument and opening the result page for the keyword in google search
import webbrowser as wb #webbrowser to access the web browser
import sys #sys to take the keyword given as argument if any

args = sys.argv

if(len(args)>1): #if there's a keyword passed through command line argument
    search = ''.join(args[1:])
    wb.open("https://www.google.com/search?&q="+search)
else: 
    search = input("Search on google:") #else takes the keyword by asking the user
    wb.open("https://www.google.com/search?&q="+search)