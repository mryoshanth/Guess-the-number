# Guess-the-number

import random
again = True

while again:
    number = random.randint(1, 5)
    print("Guess the number between 1 to 5")
    user_input = input()
    try:
        user_input = int(user_input)
    except ValueError:
        print(user_input, "is not a number, try again.")
        continue
    while user_input != number:
        if user_input > number:
           print("   ")
           print("That's too high, try again.")
           user_input = int(input())
        elif user_input < number:
           print("   ")
           print("That's too low, try again.")
           user_input = int(input())
        else:
            break
    else:
        print("   ")
        print("Good guess, the correct number is ",user_input)
        print("Wanna have another go?")
        again = ("y" or "yes") in input().lower()


print("Good game, see ya!")
