from matplotlib import pyplot as plt 

plt.style.use('fivethirtyeight')

days = [1,2,3,4,5,6,7,8,9,10] 
#the x-axis of the plot

labels = ['dev1','dev2','dev3']
#labels for the plot

dev1 = [3,5,2,3,4,5,1,2,3,1]
dev2 = [6,5,3,1,8,2,6,1,3,0]
dev3 = [2,6,4,3,8,3,2,1,2,4]
# these are the data on the y-axis
# devs work hours 

plt.stackplot(days,dev1,dev2,dev3,labels=labels)
#this is how you make a stackplot

plt.xlabel('Days')
plt.ylabel('Time worked (Hrs)')
plt.title('Developers work chart')

plt.legend()
plt.tight_layout()
plt.show()