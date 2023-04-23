import random

prenum = random.randint(1,100)

print("---------------Guess the NUMBER---------------")
print()
print("""Instructions:
        1.The Computer chooses a number from 1 to 100,You have to find it
        2.If the number you guessed is 10 numbers within the guessed number the computer prints Hot to help you
        3.2.If the number you guessed is 5 numbers within the guessed number the computer prints Hotter 
        3.Or else it prints Cold\n\n""")
i = 0
num = int(input("Guess the Number:"))

while(1):
    i += 1
    if(num == prenum):
        print("WoW,You are Right")
        if i == 1:
            print(f"You made it in the first iteration")
        else:
            print(f"You made it in {i} iterations")
        break
    elif(abs(num-prenum)<=5):
        print("Hotter")
    elif(abs(num-prenum)<=10):
        print("Hot")
    else:
        print("Cold")
    num = int(input("\nGuess the Number:"))
    
