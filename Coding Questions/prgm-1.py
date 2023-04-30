# A program to find the short form of a given word in a specific format.The conditions are given below
# Adjacent letters of a string are paired.From each pair one letter is selected
# The letter with highest ascii value is selected
# The letter is stored into str1 variable
# If a pair cannot be formed, then the last letter is added to str1




x = input()
n = len(x)
#print(n)
#print(ord(x[0]))
str1 = ''
for i in range(0,n,2):
    if(i+1 < n):
        if(ord(x[i]) > ord(x[i+1])):
            str1 = str1 + x[i]
        elif(ord(x[i]) < ord(x[i+1])):
            str1 = str1 + x[i+1]
        elif(ord(x[i]) == ord(x[i+1])):
            str1 = str1 + x[i]
    else:
        str1 = str1 + x[n-1]
print(str1)
            
