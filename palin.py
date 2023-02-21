def is_palindrome(text):
    return text == text[::-1]

with open('try.txt', 'r') as file:
    text = file.read()

words = text.split("\n")

palindromes = []
for word in words:
    if is_palindrome(word):
        palindromes.append(word)
print(palindromes)
if palindromes:
    for palindrome in palindromes:
        print(palindrome)



