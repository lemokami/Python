class Weight(): #Weight class
    def Getweight(self): #Getweight function to return the weight 
        return self.weight
        #self is used as a placeholder the same element which the 
        # function is called like x.GetWeight() x is accessed by self here

p1 = Weight() #making an object of Weight class
print(f"Instantiated an Object:: {p1}")

p1.weight = 65 #creates a weight inside the p1 object of Weight class
print(f"Person's Weight::{p1.Getweight()}") #return the weight of p1 object 