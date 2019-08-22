print("Enter anything But character cause an Error")

while(1):
    try:
        num =  int(input("\nEnter:"))
        print(f"\n{num}/2 is:: {num/2}")
        break
    except:
        print("I warned You but you didn't listened")