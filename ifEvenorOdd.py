#checks if a given number is even or not 
num = int(input("Enter your number:")) #input takes a string value so it must be casted to int

if(num % 2 == 0): #if number / 2 gives a remainder 0 it is even else odd
    print("Even")
else:
    print("odd")