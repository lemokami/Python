from matplotlib import pyplot as plt #importing matplotlib

dev_x = [10,20,30,40,50,60] #x values

dev_y = [100,300,400,700,800,1000] #y values

plt.plot(dev_x,dev_y) # making the plot

plt.xlabel('Age') #setting x axis name
plt.ylabel('Average Salary (USD)') #setting y axis name
plt.title("Programmer Salary") #title of the plot

plt.show() #displaying the plot