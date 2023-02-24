import re

stringer = "I am name is Mercy. My email addresses are nattD56dd@gmail.com, he!you@gmail.com and halooo@wowwz.ke  .My phone numbers are (072) 962 4197, (077) 482 0105 "
user_input = str(input("What do you want to do? "))

def extract_email_addresses(stringer):
    pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com)"
    return re.findall(pattern, stringer)

def extract_email_addresses(stringer):
    pattern = "(?\d{3})?[-.\s]?\d{3}[-.\s]?\d{4}"
    return re.findall(pattern, stringer)

def replace_email_addresses(stringer, replacement):
    pattern = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com)"
    return re.sub(pattern, replacement, stringer)

if user_input() == "Extract Phone Numbers":
    print("These are the phone numbers: ", extract_phone_numbers(stringer))
elif user_input() == "Extract Email Addresses":
    print("These are the email addresses: ",extract_email_addresses(stringer)) 
elif user_input == "Replace Email Addresses":
    replacement = input("Enter what you wish to replace: ")
    print("These are the replaced email addresses: ", replace_email_addresses(stringer, replacement))
else:
    print("Check your inputs and try again.")    


