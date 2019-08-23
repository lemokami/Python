#This program swaps given two numbers

#taking input
num1 = input("Enter the first number:")
num2 = input("Enter the second number:")

print()
print(f"Number before swapping num1:{num1} num2:{num2}\n") #number before swapping

num1,num2 = num2,num1 #used multiple variable assignment in python for swapping 

print(f"Number after swapping num1:{num1} num2:{num2}") #number after swapping