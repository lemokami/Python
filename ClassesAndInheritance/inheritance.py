
curr_year = 2019 #making a variable to specify current year to find the birth year

class Human(): #making the parent class human

    def __init__(self,name,age): #takes in name and age as the properties

        self.name = name
        self.age = age

    def GetBirthYear(self): #GetBirthYear method in this class finds out the birthYear of the Human
        return(curr_year - self.age) #uses the cur_year variable outside the class

class Student(Human): 
    #Student Class that inherits the properties from the Human parent class Student(Human) at first means that Student is a child/subclass of the parent Human which is in the brackets
    #Moreover,the child class will have all the methods as the parent class but the parent class will not have the methods of the child class
    #compare it with the real life to understand your Dad/Mom will not have the abilities like coding or anything like you but you have most of the properties as your parents
    
    def __init__(self,name,age,cclass): #__init__ method to add properties,takes name age and cclass as values 
        Human.__init__(self,name,age) 
        #name and age are not exclusive for Student they are the properties of the parent class
        #so you should pass the properties to parent class as here,No extra assignment needed for them hereafter 
        #since,it is created at this instance 
        
        self.cclass = cclass #since this is a property of this class only we have to assign it

    def __str__(self): # returns the string when object is made
        return("{} is in {} grade and was born in {} and is {} years old".format(self.name,self.cclass,self.GetBirthYear(),self.age))
        #from here we can see that the child class can have the parent's properties as well as methods
        #we can call the parents methods from here to find the birthyear(here)


Sam  = Student("Sam Benedict",15,10) #makes an object of class Student which is a child of Human class 

print(Sam) #prints what is returned from the __str__ in the class