import requests as req
import bs4

try:
    resp = req.get('https://automatetheboringstuff.com/files/rj.txt')
except:
    print("Network Connetion Error")
    exit(0)

fp = open("text.txt",'wb')

for piece in resp.iter_content(100000):
    fp.write(piece)

fp.close()