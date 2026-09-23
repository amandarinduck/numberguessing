import random
import sys

choice = random.randint(1, 100)


def guesses():
    difficulty = input(
        "select difficulty\neasy(10 chances)\nmedium(5 chances)\nhard(3 chances)\n"
    ).lower()
    if difficulty == "easy":
        value = 10
    elif difficulty == "medium":
        value = 5
    elif difficulty == "hard":
        value = 3
    else:
        print("Invalid. exiting...")
        sys.exit()
    for i in range(value):
        x = int(input("I'm thinking of a number between 1 and 100, what is it?\n"))
        if x == choice:
            print("Congrats!")
            break
        elif x > choice:
            print(f"Incorrect! {x} is greater than the number")
            continue
        elif x < choice:
            print(f"Incorrect! {x} is less than the number")
            continue
        else:
            print("invalid value")
            continue
    print(f"the number was {choice}")


if __name__ == "__main__":
    guesses()
