import random
from data import data
from art import logo, vs


def format_data(account):
    """ Takes the account data and returns into printable format"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"     #returns True of False
    elif a_followers < b_followers:
        return guess == "b"


# display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# make game repeatable
while game_should_continue:
    # generate random account from the game data
    # making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # ask user for guess
    guess = input("Who has more followers: Type 'A' or 'B': ").lower()

    # check if user is correct
    # 	get the follower account of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # 	use if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right. Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Your final score: {score}.")

    # score keeping
    #
    # make the game repeatable
    #
    # making the accounts at position B become the next account at position A.