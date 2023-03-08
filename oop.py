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

props = Inventory(name, quantity, price)
props.names()
props.quantities()
props.prices()

item = [name, quantity, price]

IMS = []

# Read IMS from CSV
with open('rims.csv', 'r', newline='') as f:   
    reader = csv.reader(f)
    IMS = [row for row in reader]

# Append new item to IMS
IMS.append(item)

# Write updated IMS to CSV
with open('rims.csv', 'w', newline='') as f:   
    writer = csv.writer(f)
    writer.writerows(IMS)

def display_items():
    for item in IMS:
        print(item)

def delete_item():
    for item in IMS:
        if item.name == name:
            IMS.remove(item)
        else:
            print("Item does not exist.")  

def add_item():
    for item in IMS:
        if item not in IMS:
            IMS.append(item)
            # Write updated IMS to CSV
            with open('rims.csv', 'w', newline='') as f:   
                writer = csv.writer(f)
                writer.writerows(IMS)
        else:
            print("Item exists.")

display_items()
add_item()




