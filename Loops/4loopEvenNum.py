
print("Hello There,Here we are making a series of even numbers upto a given number\n\n")

lim = int(input("Enter the last no of the series:")) #we have to cast input to int since input takes in string character

# for loop ,range has three parameters 1.lower limit 2.upper limit 3.step

for i in range(2,lim,2): 
    print(f"{i}\t",end = "") 
    
    # end is used to secify the character at the end of the print statement (default is \n)
    # fstrings was introduced in python3 which makes printing more simple 

print() # for printing \n at last
