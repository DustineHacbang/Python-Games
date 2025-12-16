# print("Hello World")
import random
value =input("Would you like to play the  python dice rolling game? (yes/no): ")
if value == "yes":
    while value == "yes":
        dice_val = [1,2,3,4,5,6]
        print (" Lets play the game")
        print (" The dice is rolling...")
        print (random.choice(dice_val))
        value = input("Would you like to keep rolling? (yes/no): ")
        if value == "no":
            print (" Thank you for playing the game, come back soon!")
            break
        elif value != "yes":
            print (" Please enter a valid response")
            break
elif value != "no":
    print (" Please enter a valid response")
else:
    print (" Thank you for playing the game, come back soon!")
