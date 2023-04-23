#checks if a given number is even or not 
num = int(input("Enter your number:")) #input takes a string value so it must be casted to int

if (n&1):          # ANDing with 1 checks if a number is odd , useful for large numbers 
    print("odd")
else:
    print("even")
