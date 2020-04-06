from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
#using a prebuilt theme

slices = [59219, 55466, 47544, 36443,35917]
#these are the data for the pie chart pie will automatically covert it into percentage
 
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# these are the labels for the data we injected
# they should be of the same order as of the data list

plt.pie(slices,labels=labels,autopct="%1.1f%%",explode=[.1,0,0,0,0],shadow=True,wedgeprops={"edgecolor":"black"})
# .pie plots a pie chart 
# labels is the labels or the names we passed
# explode moves the piece of the pie from the pie by the given list of order of the data
# shadow gives shadow as the name suggests
# wedgeprops is a dictionary of properties of wedge we use "edgecolor" to color the edges
# autopct displays the %  values to the pie-plot
  
plt.title("Programming languages and it's average userbase (2019)")
plt.tight_layout()
plt.show()