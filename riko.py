def is_palindrome(text):
    """
    A function that checks if a given string is a palindrome.
    """
    return text == text[::-1]

# Open the file and read its content
with open('try.txt', 'r') as file:
    text = file.read()

# Split the text into words
words = text.split()

# Find all palindromes in the text
palindromes = []
for word in words:
    if is_palindrome(word):
        palindromes.append(word)

# Print all the palindromes found
if palindromes:
    print("The palindromes in the file are:")
    for palindrome in palindromes:
        print(palindrome)
else:
    print("No palindromes found in the file.")
