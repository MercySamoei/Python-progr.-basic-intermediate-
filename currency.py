def usd_to_ksh(num1):
    return num1 * 112.50

def euro_to_ksh(num2):
    return num2 * 132.45

def euro_to_usd(num3):
    return num3 * 1.20

preferred_destination = ['Euro to Ksh', 'Euro to USD','USD to Ksh']
choice = input("Enter your preferred destination: ")
amount = float(input("Enter the amount: "))

if choice == preferred_destination[0]:
    print(amount, "Euro is equal to", usd_to_ksh(amount), "Ksh")
elif choice == preferred_destination[1]:
    print(amount, "Euro is equal to", euro_to_ksh(amount), "USD")
elif choice == preferred_destination[2]:
    print(amount, "USD is equal to", euro_to_usd(amount), "Ksh")
else:
    print("Invalid choice. Please choose one of the following: ", preferred_destination)
    
