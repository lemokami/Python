class WeightHeight(): #class creation
    def __init__(self,w,h): #takes height and weight 
        self.weight = w
        self.height = h

    def inGmCm(self): #coverts the height and weight to Gm and Cms 
        return WeightHeight(self.weight*1000,self.height*100)
        #returns another object of the same class(instance ad return values)
    
    def __str__(self): #str constructor
        return("Weight is:::{}\nHeight is:::{}\n".format(self.weight,self.height))
    
    def Bmi(self): #function to calculate Bmi
        return(self.weight/(self.height * self.height))

p1 = WeightHeight(75,1.5) #making an object p1
print(p1)
print("---In Gm and Cm---")
small = p1.inGmCm()#another object small which is made by the fuction inCmGm
print(small)
print("\nBmi is:::{}\n".format(p1.Bmi())) #uses bmi function in the class
