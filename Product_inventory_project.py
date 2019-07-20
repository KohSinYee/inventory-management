#Product Inventory Project - Create an application which manages an inventory of products.
#Create a product class which has a price, id, and quantity on hand.
#Then create an inventory class which keeps track of various products and can sum up the inventory value.
import shelve



##Create product class.
class Product:
    def __init__(self, ID, name, price, quantity):
        self.id = ID
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.records = {}       # id --> Product

    def add(self, ID, name):
        self.records[ID] = name

    def add_new_product(self,name, price, quantity):
        global current_ID
        current_ID = current_ID + 1                                         # generate id
        name = Product(current_ID,name, price,quantity)                     # generate new product
        self.add (current_ID, name)
        return current_ID
        return name

    def add_quantity (self, ID,name, quantity):
        if ID == False:
            print ("ID is not found, please add new product.")
        else:
            self.records[ID].quantity = int(self.records[ID].quantity) + int(quantity)                #update new quantity

    def change_price (self, ID,name, new_price):
        if ID == False:
            print ("ID is not found, please add new product.")
        else:
            self.records[ID].price = new_price                                  #new_price

    def summary(self):
        print("ID    Name  Price  Quantity")
        for key in self.records:
            print ("%s  :: %s :: %s :: %s" %(key,self.records[key].name, self.records[key].price, self.records[key].quantity))


storage = shelve.open('store', writeback=True)

inventory = None
if 'inventory' in storage:
    inventory = storage['inventory']
else:
    inventory = Inventory()

current_ID = len(inventory.records)

while True:
    
    print("Functions:\n1) Add New Product\n2) Update quantity\n3) Update Price\n4) Summary")
    x = int(input())

    if x == 1:
        print("Please enter name,price and quantity in order (with comma).")
        y = input()
        y = y.split(",")
        inventory.add_new_product(y[0],y[1],y[2])

    if x == 2:
        print("Please enter ID,name,changes in order (with comma).")
        y = input()
        y = y.split(",")
        inventory.add_quantity(y[0],y[1],y[2])

    if x == 3:
        print("Please enter name,updated price (with comma).")
        y = input()
        y = y.split(",")
        inventory.change_price (y[0],y[1],y[2])

    if x == 4:
        inventory.summary()

    print ("Continue? Y/N")
    z = input()
    if z.lower() != 'y':
        break
    
storage.close()

#check ID to name
# store to file (cannot do yet)
