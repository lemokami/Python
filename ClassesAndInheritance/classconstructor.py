class NumberSet(): #number set class
    def __init__(self,num1,num2): 
        #__init__ is a parameterized constructor
        #It is always called when an object is created
        self.num1 = num1 
        self.num2 = num2
    
t = NumberSet(6,10) #creates a class object as well adding values to it at the same time
#__init__replaces t.num1=num1 and t.num2=num2

print(f"NumberSet:::{t.num1,t.num2}") #prints the numbers

# Types of constructors :

# 1.default constructor :The default constructor is simple constructor which 
#                        doesn’t accept any arguments.It’s definition has only
#                        one argument which is a reference to the instance being constructed.
#     
# 2.parameterized constructor :constructor with parameters is known as parameterized
#                              constructor.The parameterized constructor take its first
#                              argument as a reference to the instance being constructed
#                              known as self and the rest of the arguments are provided by
#                              the programmer.
