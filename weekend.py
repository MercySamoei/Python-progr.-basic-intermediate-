import csv

class Inventory:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def names(self):
        print(f"{self.name} is the name of the IMS")

    def quantities(self):
        print(f"{self.quantity} is the quantity")

    def prices(self):
        print(f"{self.price} is the price")


name = input("Input the name of the IMS: ")
quantity = int(input("Input the quantity: "))
price = int(input("Enter the price: "))

item=[name, quantity, price]
print(item)

features = Inventory(name, quantity, price)
features.names()
features.quantities()
features.prices()

def add_an_item():
    name = input("Enter the name of the item you want to add: ")
    quantity = int(input("Enter the quantity: "))
    price = int(input("Enter the price: "))

    for item in IMS:
        if name == item[0]:
            print(name, "exists")
            return IMS
    IMS.append([name, quantity, price])
    with open('IMS.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, quantity, price])
    print(name, "has been added")
    return IMS        

IMS =[['Bike', '10', '1000'],['Skates', '5', '2000'],['Phone', '2', '1500']]


def remove_an_item():
    name = input("Enter the name of the item you want to delete: ")
    for item in IMS:
        if name == item[0]:
            IMS.remove(item)
            print(item, "has been removed") 
            return IMS
    print(name, "does not exist")
    return IMS

def display_inventory():
    for item in IMS:
        print(item)
    return IMS

remove_an_item()
display_inventory()
