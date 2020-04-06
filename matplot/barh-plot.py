from matplotlib import pyplot as plt
import csv # for dealing with csv files
from collections import Counter
# for finding data from csv

plt.style.use('fivethirtyeight')


with open('data.csv',"r+") as cf:
    # opening files
    
    data = csv.DictReader(cf)
    #reades the file in a dictionary format
    
    lang_data = Counter()
    #making a counter

    for row in data:
        lang_data.update(row['LanguagesWorkedWith'].split(';'))
        #updates the counter 

lang = [] #for storing the name of the languages people uses
users = [] #for storing the number of users

for language in (lang_data.most_common(10)):
    # most common selects the top users from the counter
    lang.append(language[0])
    users.append(language[1])

#reversing the lists for display purposes
lang.reverse()
users.reverse()

plt.barh(lang,users) # barh is barh'orizontal'

plt.title("Top 10 Programming Languages")
plt.xlabel("Users")
plt.ylabel("Languages")
plt.tight_layout()
plt.show()