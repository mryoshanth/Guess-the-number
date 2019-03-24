import random
again = True

while again:
    guess_taken = 0
    number = random.randint(1, 5)
    print("\nGuess the number between 1 to 5")
    user_input = input("Number (1-5):")
    guess_taken += 1
    try:
        user_input = int(user_input)
    except ValueError:
        print(user_input, "is not a number, try again.")
        continue
    while guess_taken < 9:
        if user_input > number:
           print("\nThat's too high, try again.")
           user_input = int(input("Number (1-5):"))
           guess_taken += 1
        elif user_input < number:
           print("\nThat's too low, try again.")
           user_input = int(input("Number (1-5):"))
           guess_taken += 1
        else:
            print("   ")
            print("Good guess, the correct number is", user_input)
            if guess_taken > 1:
                print("You guessed it right in", guess_taken, "attempts.")
            else:
                print("You guessed it right in", guess_taken, "attempt.")
            break
    else:
        print("You have reached the maximum number of tries.")

    print("\nDo you wanna play again?")
    again = ("y" or "yes") in input().lower()

print("Good game, see ya!")