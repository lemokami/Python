#Some common python string methods

string = input("Enter a string:") #taking a string to work with

print(f"Splitted string:{string.split()}") #using .split() method to split the string in to words

print(f"\nTitle cased:{string.title()}") #.title() turns the first letter of each word in the string to an uppercase

print(f"\nUpper Cased:{string.upper()}") #.upper() turns every letter in the string to uppercase

print(f"\nLower Cased:{string.lower()}") #.lower() turns  every letter in the string to lowercase

print(f"\nrjust-ed:{string.rjust(20,'-')}") 
#.rjust(width,[fillchar])  returns the string right justified in a string of length width.
# Padding is done using the specified fillchar (default is a space)

print(f"\nljust-ed:{string.ljust(20,'-')}")
#.ljust(width,[fillchar])  returns the string left justified in a string of length width. 
# Padding is done using the specified fillchar (default is a space)

print(f"\ncenter-ed:{string.center(20,'-')}")
#.center(width,[fillchar])  returns the string centered in a string of length width. 
# Padding is done using the specified fillchar (default is a space)
