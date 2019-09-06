#This program helps to understand the scope of global and local variables

def some_func(): #some function
    python = 3.7 #a local variable
    global jdk #global jdk variable
    jdk = 12 # changing value
    print(f"Vaue of python in fumction is {python} (local not same as outside the function)")

python = 2.6 #global variable (can't be accessed unless called by global keyword)
jdk = 12

#printing the values before running the function
print(f"value of python outside the function is {python} ")

print(f"value of jdk before running the function is {jdk}")

print("\n---------------------------------------------------\n")

#printing the values after running the function 

some_func() #calling the function

print(f"value of jdk after running the function is {jdk} (global changed)\n") 
