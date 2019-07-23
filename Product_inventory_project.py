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

    def add(self, ID, product):
        self.records[ID] = product

    def add_new_product(self, name, price, quantity):
        new_ID = len(self.records)                                      # generate id
        new_product = Product(new_ID, name, price,quantity)                     # generate new product
        self.add (new_ID, new_product)
        return new_ID

    def add_quantity (self, ID, name, quantity):
        if ID not in self.records:
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

while True:

    print("Functions:\n1) Add New Product\n2) Update quantity\n3) Update Price\n4) Summary")
    x = int(input())

    if x == 1:
        print("Please enter name,price and quantity (whole number) in order, separated with commas.")
        y = input()
        y = y.split(",")
        inventory.add_new_product(y[0],float(y[1]),int(y[2]))

    if x == 2:
        print("Please enter ID,name,changes in order (with comma).")
        y = input()
        y = y.split(",")
        inventory.add_quantity(int(y[0]),y[1],int(y[2]))

    if x == 3:
        print("Please enter id, name,updated price (with comma).")
        y = input()
        y = y.split(",")
        inventory.change_price(int(y[0]),y[1],float(y[2]))

    if x == 4:
        inventory.summary()

    print ("Continue? Y/N")
    z = input()
    if z.lower() != 'y':
        break

storage['inventory'] = inventory
storage.close()

#check ID to name
# store to file (cannot do yet)
