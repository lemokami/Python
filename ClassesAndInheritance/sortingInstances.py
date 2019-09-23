class items():
#making a class item to store the prices of some items
    def __init__(self,name,price): #takes itemname and price
        self.name = name
        self.price = price

lis = [ #list of instances of items class
    items("apple",20),
    items("lego",5),
    items("pepsi",15)
]

for item in sorted(lis,key = lambda x : x.price): #key is the price,the list is sorted by price in ascending order
    print("{} => {}".format(item.name,item.price))
