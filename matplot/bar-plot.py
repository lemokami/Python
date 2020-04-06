from matplotlib import pyplot as plt
import numpy as np # importing numpy for some reasons (can't display two bars at the same time cleanly)

plt.style.use('fivethirtyeight') #prebuilt theme

# python developer data from stackoverflow survey 
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850] 

# javascript developer data from stackoverflow survey 
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823]

# ages of developers 
ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

x_label = np.arange(len(ages_x)) # making a numpy array for removing the two bar issue
width=0.25 # custom width

plt.bar(x_label-width,py_dev_y,width=width,label="Python") 
# x_label-width is used for showing two bars the bar will be at x_label-width than the next bar which is at x_label

plt.bar(x_label,js_dev_y,width=width,label="JavaScript")
# width is an argument for custom width and .bar is used for bar plot


plt.title("Median Salary Per Age")
plt.xlabel("Ages")
plt.ylabel("Salary Per Year (USD)")

plt.xticks(ticks=x_label,labels=ages_x) 
# making x axis from the real data since we used the numpy array at first

plt.legend()
plt.tight_layout()
plt.show()