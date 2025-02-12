print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
userInput = input("There are two paths ahead of you which would you like to go? Left or Right? ").lower()

if userInput == "right":
    print("You fell into a hole! Game Over.")
elif userInput == "left":
    print("You find yourself in a cavern. The only way through is past a quickly flowing river.")
    userInput = input("Do you attempt to swim across or wait? Swim or Wait? ").lower()
    if userInput == "swim":
        print("You were attacked by a trout! Game Over.\n")
    elif userInput == "wait":
        print("You approach a door. To the right of the door are three buttons.")
        print("One is red, one is yellow, and one is red. Which button do you press?")
        userInput = input("Red, Yellow, or Blue? ").lower()
        if userInput == "red":
            print("You are burned by fire! Game Over.")
        elif userInput == "blue":
            print("You are eaten by beasts! Game Over.")
        elif userInput == "yellow":
            print("The door opens and you find a massive pile of treasure behind it! You Win!")
        else:
            print("Incorrect input; exiting.")
    else:
        print("Incorrect input; exiting.")
else:
    print("Incorrect input; exiting.")