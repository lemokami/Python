#this program swaps the characters in the given string
string = input("Enter your string to be case-swapped:")

newstring = str() #since,string is immutale we use a new string for storing the swapped string

for ch in string: #loop to take each character
    
    if (ch.isupper()): #checking if the character is an uppercase character
        newstring += ch.lower() #using .lower() to change the character to lower-case and adding to newstring
    
    elif (ch.islower): #checking if the character is a lowercase character
        newstring += ch.upper() #using .upper() to change the character to upper-case and adding to newstring

print(newstring) #printing the new string

