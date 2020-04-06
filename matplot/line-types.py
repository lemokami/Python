from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight') #taking a builtin style

year_x = [1800,1825,1850,1875,1900,1925,1950,1975,2000]

mort_y = [30,25,27,26,20,40,37,25,17]
plt.plot(year_x,mort_y,label="India",linestyle='--') 
#linestyle determines the style of the plotted line

mort_y = [10,13,14,15,12,11,16,17,15]
plt.plot(year_x,mort_y,label="Europe",linestyle='-.')
#a shorthand is "{color}{marker}{linestyle}" to change three properties

plt.xlabel("Year")
plt.ylabel("Infant Mortality Rate (%)")
plt.legend()
plt.tight_layout() #resolves the padding issue if found 
plt.show()