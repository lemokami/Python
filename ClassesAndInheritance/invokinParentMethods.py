#Accessing parent's methods from the child class' instance
#make sure you read inheritance.py first
curr_year = 2019 #making a variable to specify current year to find the birth year

class Human(): #making the parent class human

    def __init__(self,name,age): #takes in name and age as the properties

        self.name = name
        self.age = age

    def GetBirthYear(self): #GetBirthYear method in this class finds out the birthYear of the Human
        return(curr_year - self.age) 

class Student(Human): 
    
    
    def __init__(self,name,age,cclass): #__init__ method to add properties,takes name age and cclass as values 
        Human.__init__(self,name,age) 
        self.cclass = cclass 

    def GetBirthYear(self): #to access the method of the parent by the object of the parent we use the below code 
        self.year = Human.GetBirthYear(self) #we call the method from here of the parent
        return("Birth Year:: {}".format(self.year)) #returns it to the user when object is called
    
    def __str__(self): 
        return("{} is in {} grade and is {} years old".format(self.name,self.cclass,self.age))
        


Sam  = Student("Sam Benedict",15,10) #makes an object of class Student which is a child of Human class 

print(Sam) #prints what is returned from the __str__ in the class

print(Sam.GetBirthYear()) #prints the birthyear of the object which is found out by the method in the parent class