from art import hl, vs
from HLG_data import data
from random import randint
from replit import clear

list_index = []
MAX_Score = len(data) - 2


def clear_print():
    clear()
    print(hl)


# function for validate answer
def validate(respond, validate_list):
    if respond in validate_list:
        return True
    else:
        print("\nOpss! You choose an invalid option! Try again!")
        return False


# function for display opponents
def display_opponents(opponents):
    print(
        f"Compare A: {opponents[0]['name']}, {opponents[0]['description']}, from {opponents[0]['country']}")
    # print(f"{opponents[0]['follower_count']} ")
    print(vs)
    print(
        f"Against B: {opponents[1]['name']}, {opponents[1]['description']}, from {opponents[1]['country']}")
    # print(f"{opponents[1]['follower_count']} ")


def get_unique_index():
    while True:
        index = randint(0, len(data)-1)
        if index in list_index:
            continue
        else:
            list_index.append(index)
            return index


# function for getting the opponents
def get_opponents():
    opponents = []
    for i in range(2):
        index = get_unique_index()
        opponents.append(data[index])
    return opponents


def change_opponents(opponents, winner, score):
    index = get_unique_index()
    opponents[0] = winner
    opponents[1] = data[index]

    user_choice(opponents, score)


def get_winner(opponents, potential_winner, score):
    a = opponents[0]['follower_count']
    b = opponents[1]['follower_count']

    winner_verification = 'a' if a > b else 'b'
    winner = opponents[0] if a > b else opponents[1]

    if winner_verification == potential_winner:
        score += 1
        clear_print()
        print(f"You're right! Current score: {score}.")
        if score == MAX_Score:
            print(f"You Win with a maximum score: {score}")
        else:
            opponents = change_opponents(opponents, winner, score)
    else:
        clear_print()
        print(f"Sorry, that's wrong. Final score: {score}")


# function for determinating the right answer
def user_choice(opponents, score):
    display_opponents(opponents)
    while True:
        potential_winner = input(
            "Who has more followers? Type 'A' sau 'B': ").lower()
        if validate(potential_winner, ["a", "b"]):
            break
    get_winner(opponents, potential_winner, score)


# function for play again
def play_again():
    while True:
        answer = input(
            "\nDo you want to play again? Please type 'y' for yes or 'n' for no: ").lower()
        if validate(answer, ["y", "n"]):
            return answer == "y"


# main function
def higher_lower():
    global list_index
    while True:
        score = 0
        list_index = []
        clear_print()
        opponents = get_opponents()
        user_choice(opponents, score)
        if not play_again():
            print("See you next time!")
            break


higher_lower()
