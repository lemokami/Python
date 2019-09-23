class Cereal(): #making a cereal class
    def __init__(self,name,brand,fiber): 
        self.name = name
        self.brand = brand
        self.fiber = fiber
    
    def __str__(self): #returns to the object when the object is created
        return ("{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name,self.brand,self.fiber))
    
c1 = Cereal("Corn Flakes","Kellogg's",2) #the return value in __str__ is saved in c1 which is a string
c2 = Cereal("Honey Nut Cheerios","General Mills",3) #the return value in __str__ is saved in c2 which is a string

print("c1::{}\n\nc2::{}".format(c1,c2))