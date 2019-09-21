#methods and attributes used in numpy
import numpy as np

arr = np.arange(0,100,2)#creates a numpy array of even numbers from 0 to 101 

print(f"Old Array:::\n{arr}\n")

arr = arr.reshape(5,10)
# .reshape reshapes the array to the given dimentions 
# if the dimentions all the elements to fit inside it like for (m,n) 
# mxn should be equal to the no of elemets in the array to be reshaped

print(f"ReShaped array to 5x10 matrix using reshape:::\n{arr}\n")

print(f"Shape of the array found using shape:::{arr.shape}\n")
#.shape returns the dimentions of the array,it takes no arguments
 
print(f"Max of the array:::{arr.max()}\n")
#.max() returns the highest element in the array

print(f"Min of the array:::{arr.min()}\n")
#.min() returns the lowest element in the array

print(f"Index of the highest element in the array:::{arr.argmax()}\n")
#.argmax() returns the index the highest element in the array

print(f"Index of the lowest element in the array:::{arr.argmin()}\n")
#.argmin() returns the index the lowest element in the array

print(f"Data type of the elements is:::{arr.dtype}")
#returns the data type of the array here int64