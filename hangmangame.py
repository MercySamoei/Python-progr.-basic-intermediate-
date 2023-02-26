import random

project = ('Ball' ,'modern', 'comp', 'are', 'collect', 'of', 'pieces', 'nurse', 'run', 'of', 'board', 'chips', 'band', 'other', 'devices', 'mom', 'all', 'these', 'pieces', 'are', 'called', 'thow')

def four_letter_words():
    result = []
    for word in project:
        if len(word) == 4:
            result.append(word)
    return result

def five_letter_words():
    result = []
    for word in project:
        if len(word) == 5:
            result.append(word)
    return result

def six_letter_words():
    result=[]
    for word in project:
        if len(word) == 6:
            result.append(word)
    return result    

print("This is the hangman game #insert something funny#")
options="1. Four letter words \n2. Five letter words \n3. Six letter words"
print(options)
choice = int(input("Enter your choice: "))

if choice == 1:
    word=random.choice(four_letter_words())
elif choice == 2:
    word=random.choice(five_letter_words())
elif choice == 3:
    word=random.choice(six_letter_words())
else:
    print("Invalid choice, try again.")

unknown_word= "-" * len(word)
correct_guesses = []
incorrect_guesses = []
while True:
    #print("\n" + unknown_word)
    print("Correct guesses: " + ", ".join(correct_guesses))
    print("Incorrect guesses: " + ", ".join(incorrect_guesses))

    guess = input("Guess a letter: ").lower()

    if guess.lower() in word.lower():
        for i in range(len(word)):
            if word[i] == guess.lower():
                unknown_word = unknown_word[:i] + word[i] + unknown_word[i+1:]
        correct_guesses.append(guess)
        if unknown_word == word:
            print("You guessed the word "  + word + " and won the game!")
            break
    else:
        incorrect_guesses.append(guess)
        if len(incorrect_guesses) >= 6:
            print("\nSorry, you have run out of guesses. The word was \"" + word + "\".")
            break
        else:
            print("Incorrect guess. Please try again.")


