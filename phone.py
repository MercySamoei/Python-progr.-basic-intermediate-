options=['Add a contact','Delete a contact','Search a contact','View the contact list']
choice=input("What do you want to do? ")

phonedict = {
    'Mercy': '0729','Koi': '0702','Elon': '0757','Yono': '0798'
    }

def add_a_contact():
    name=str(input("Enter the name: "))
    contact=int(input("Enter the contact: "))
    if name in phonedict: 
        print(name, "already exists") 
    else:    
       phonedict[name]=contact
       print(name, "has been added")
    return phonedict

def delete_a_contact():
    name = str(input("Enter the name: "))
    if name in phonedict:
        phonedict.pop(name)
        print(name, "has been deleted")
    else:
        print(name, "not found. Try again.")
    return phonedict 

def search_a_contact():
    name =str(input("Enter the name: "))
    if name in phonedict:
        phonedict.get(name) 
        print(name, ":", phonedict[name])
    else:
        print(name, "does not exist")  

def view_contact_list():
    for name, contact in phonedict.items():
        print(name, ":", contact)

if choice == options[0]:
    print(add_a_contact())
if choice == options[1]:
    print(delete_a_contact())   
if choice == options[2]:
    print(search_a_contact())
if choice == options[3]:
    print(view_contact_list())
else:
    print("Input the right choice.")
