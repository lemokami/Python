#This program uses a dictionary to store the letter count in key value pairs and prints it
import pprint as pp #for pretty printing

let = dict() #an empty dictonary to store the letter count data

string = input("Enter the string:")

for ch in string: #loop to iterate through each letter
    
    let.setdefault(ch,0) #sets 0 value to the given key if the key does not exist in the dictionary
    let[ch] += 1 #for each letter  in the string adds the count of that letter in dictionary by 1

pp.pprint(let) #uses pretty print library to pretty print the dictionary
