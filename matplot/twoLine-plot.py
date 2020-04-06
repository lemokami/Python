from matplotlib import pyplot as plt

year_x = [2000,2001,2002,2003,2004,2005,2006,2007,2008] #x axis

apple_y = [20,30,35,40,30,36,50,40,35] # first line y-axis

orange_y = [10,15,20,30,35,30,25,40,45] # second line y-axis

plt.plot(year_x,apple_y,label = "Apple Price") # plotting first line


plt.plot(year_x,orange_y,label="Orange Price") # plotting second line

plt.xlabel = "Year"
plt.ylabel  = "Price per KiloGram (KG)"
plt.title = "Prices of Fruits"
plt.legend() # makes a small box showing which line represents which
plt.show()
