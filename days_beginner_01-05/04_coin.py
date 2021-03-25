import random

print('Guess the side of the coin flip')
coin_flip = random.randint(0, 1)

if coin_flip == 0:
    print("Tails")
else:
    print("Heads")