#this program uses some common arrays in the numpy library
#you should have numpy at first
#pip/pip3 install numpy --user 
import numpy as np 

array_arr = np.array([[1,2,3],[4,5,6]])
#array in numpy creates a numpy array from a given list or matrix


arange_arr = np.arange(0,101,2)
#arange in numpy is similar to range function except it produces nubers in the numpy array 
#Here,it makes a numpy array of even numbers from 0 to 101 ,the third argument is the step like in range

zeros_arr = np.zeros((2,4))
#zeros in numpy makes a numpy array with the given dimetions(Here a 2x4 matrix) 1D,2D etc having the value of each element 0

ones_arr = np.ones((4,4))
#ones in numpy creates a numpy array with the given dimension(Here a 4x4 matrix) having the value of each element 1

linspace_arr = np.linspace(1,10,5)
#linspace in numpy creates a numpy array from a given number to a number with the given no of numbers
# i.e,linspace takes three arguments (beginning,ending,how many numbers with equal space you want to create) consecutive numbers in the array will have equal space between them

rand_arr = np.random.rand(4,2)
#rand in numpy.rand creates a numpy array in the given dimentions randomly between 0 and 1

randn_arr = np.random.randn(5,3)
#randn in numpy.randn creates a numpy array in the given dimetions randomly between a non standard distribution

randint_arr = np.random.randint(0,101,10)
#randint in numpy.random creates a numpy array between a given range(1st and 2nd arguments) and given no of numbers(3rd argument)
#they are all integers



#printing of the values
print(f"Numpy matrix with array::: \n{array_arr}\n")
print(f"Numpy array with arange:::\n {arange_arr}\n")
print(f"Numpy array of zeroes with zeros::: \n{zeros_arr}\n")
print(f"Numpy array of ones with ones::: \n{ones_arr}\n")
print(f"Numpy array using linspace::: \n{linspace_arr}\n")
print(f"Random Numpy array using random.rand::: \n{rand_arr}\n")
print(f"Random Numpy array using random.randn::: \n{randn_arr}\n")
print(f"Random Numpy array using random.randint::: \n{randint_arr}\n")
