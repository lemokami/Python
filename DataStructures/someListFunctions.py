#Some common list functions
py = ["python","django","flask"] #list1

js = ["javaScript","ReactJs","AngularJS"] #list2

print("These are our lists:")

#printing the lists
print(f"list py:{py}\n")
print(f"list js:{js}\n")

print("------------------------------")

#Using .index to find the index
findex = input("Search element in list py:")

if findex in py: #in used to check if given element is in the list
    index = py.index(findex) #finding the index in the list using .index
    print(f"{findex} is the {index+1}th element of the list py\n")
else:
    print(f"{findex} Not Found\n") #prints if element is not found

print("------------------------------")

#using append to add an element to a list (the added element is a new element and is added to the end)
val = input("Enter an element for adding in list js:")

js.append(val)
print(f"list 2 now:{js}\n")#printing the new list

print("------------------------------")

#using .insert to insert an element in a specified place
inval = input("Enter an element to be added to list py")

ind = int(input("In Which place:"))

py.insert(ind,inval)

print(f"list 2 now:{py}\n")#printing the new list

