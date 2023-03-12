#This code is a snake and ladders game. 

import random

final_position = 100
snakes = {17:7, 54:34, 62:19, 64:29, 87:36, 93:73, 95:65, 98:49}
ladders = {1:38, 4:14, 9:31, 21:42, 28:84, 51:67, 72:91, 80:99}

num_players = int(input("Number of people playing: "))
players = []
for i in range(num_players):
    player_name = str(input(f"Enter player {i+1} name: "))
    players.append((player_name, 0))

def swallowed(player, position):
    print(f"{player[0]} landed on the snake's head in tile number {position}. Sliding to tile number {snakes[position]}")
    return snakes[position]

def lifted(player, position):
    print(f"{player[0]} landed at the tail of the ladder in tile number {position}. Climbing up to tile number {ladders[position]}")
    return ladders[position]

def roll():
    return random.randint(1, 6)

def roll_number(player):
    dice_roll = roll()
    print(f"{player[0]} rolled a {dice_roll}")
    new_position = player[1] + dice_roll
    if new_position >= final_position:
        print(f"{player[0]} has reached the finish point first. Congratulations!!!")
        return final_position
    print(f"{player[0]} moved to {new_position}")
    if new_position in snakes:
        new_position = swallowed(player, new_position)
    elif new_position in ladders:
        new_position = lifted(player, new_position)
    return new_position


while True:
    for player in players:
        input(f"{player[0]}, hit enter to roll the dice.")
        player_position = roll_number(player)
        player_index = players.index(player)
        players[player_index] = (player[0], player_position)
        if player_position == final_position:
            print(f"{player[0]} has reached the finish point first. Congratulations!!!")
            break
    else:
        continue
    break




