import sys #a python library with exit() function to stop the program instantly

i = 1

while(i): #trying to make an infinite loop
    print(i)
    i+=1
    if(i>1000):
        sys.exit() #sys.exit() used to exit the program