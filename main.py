from turtle import clear

from game_data import data
from art import vs, logo
import random
import os

# test import
# print(data[1])
# print(vs)

# Welcome User
print(logo)
print("Welcome to the higher-lower game. Try to guess which account has the most followers!")


def winner():
    item1 = random.randint(0, (len(data) - 1))
    item2 = random.randint(0, (len(data) - 1))
    if item1 == item2:
        item2 = random.randint(0, (len(data) - 1))
    followers1 = data[item1]['follower_count']
    followers2 = data[item2]['follower_count']
    # print(f"Follower1 {followers1}, Follower2 {followers2}")

    # global followers1, followers2, item1, item2
    score = 0

    flag = False

    while flag is False:
        print(f"Follower1 {followers1}, Follower2 {followers2}")
        print(f"A. {data[item1]['name']}, {data[item1]['description']}, {data[item1]['country']}")
        print(vs)
        print(f"B. {data[item2]['name']}, {data[item2]['description']}, {data[item2]['country']}")
        user_choice = input(f"Which account has the most followers? 'A' or 'B'? \n").title()

        if followers1 == followers2:
            print("Tied.")
        if followers1 > followers2:
            if user_choice == 'A':
                score += 1
                clear()
                os.system('cls' if os.name == 'nt' else 'clear')
                print('That is correct.')
                print(f"Your score is: {score}\n")
                followers1 = followers2
                item2 = random.randint(0, (len(data) - 1))
                followers2 = data[item2]['follower_count']
            else:
                print(f"Game Over. Final Score: {score}\n")
                exit()
        else:
            if user_choice == 'B':
                score += 1
                clear()
                os.system('cls' if os.name == 'nt' else 'clear')
                print('That is correct.')
                print(f"Your score is: {score}")
                followers1 = followers2
                item2 = random.randint(0, (len(data) - 1))
                followers2 = data[item2]['follower_count']
            else:
                print(f"Game Over. Final Score: {score}")
                exit()


# let winner go against new random item on list


winner()
