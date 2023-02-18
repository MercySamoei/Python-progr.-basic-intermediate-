#def is_palindrome(text):
    #return text == text[::-1]

#with open('dictionary.txt', 'r') as file:
    #text = file.read()

#words = text.split(\n)

#palindromes = []
#for word in words:
    #if is_palindrome(word):
       # palindromes.append(word)

#if palindromes:
    #for palindrome in palindromes:
       # print(palindrome)


words=[]

with open('Dictionary.txt', "r") as dictwords:
    for i in dictwords.read().splitlines():
        words.append(i)
for x in words:
    if x == x[::-1]:
        print(x)




