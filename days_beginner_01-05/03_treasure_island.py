print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

turn = input("You have come to an end of the road, select which way to turn: left or right?\n").lower()
if turn == "left":
    swim_or_wait = input("Now you need to make a decision: swim or wait?\n").lower()
    if swim_or_wait == "wait":
        door = input("You have reached the final step. Select the door to open: Red, Blue or Yellow?\n").lower()
        if door == "red":
            print("You have been burned: Gamer over.")
        elif door == "blue":
            print("You have been eaten by beasts: Gamer over.")
        elif door == "yellow":
            print("You found the treasure Congratulations!. You Won!!!")
        else:
            print("There was no such door. Game over.")
    else:
        print("You have been attacked by trout. Game over.")
else:
    print("You have fallen in to a hole. Game over.")