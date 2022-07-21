class Inventory(): # This is what a class looks like
    def __init__(self): # Constructor
        self.inventoryList = []

    def add_inventory(self, item): # Method
       self.inventoryList.append(item)

    def get_inventory(self):
        return self.inventoryList

items = Inventory() # Object created from a class
items.add_inventory("ladder")
items.add_inventory("table")
print(items.get_inventory())