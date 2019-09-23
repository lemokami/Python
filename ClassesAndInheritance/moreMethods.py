class Animal(): #making an animal class
    def __init__(self,arms,legs): #constructor
        self.arms = arms #arms of the animal
        self.legs = legs #legs of the animal
    
    def limbs(self): #returns the no of limbs when called
        return self.legs + self.arms
    
spider = Animal(4,4) #making the object 
spidlimbs = spider.limbs()#calling the method limbs to get total no of lims of the animal

print(f"Number of limbs of spider are::{spidlimbs}")