#import random

choices = ['rock', 'paper', 'scissors']

user1_choice = input("Player 1 ")
while user1_choice not in choices:
    user1_choice = input("Invalid input. ")

user2_choice = input("Player 2 ")
while user2_choice not in choices:
    user2_choice = input("Invalid input. ")

if user1_choice == user2_choice:
    print("It's a tie!")
elif (user1_choice == 'rock' and user2_choice == 'scissors') or \
     (user1_choice == 'scissors' and user2_choice == 'paper') or \
     (user1_choice == 'paper' and user2_choice == 'rock'):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
