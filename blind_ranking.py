import random

command = input(
    "Welcome to \"A Ciegas\", a game of probability and logic. If you dont know how to play use the command "
    "\ --help´, if\ your arent new the you can play by using --game: ")


def game(x):
    number_list = ["","","","",""]
    number = random.randint(1, x)
    position = int(input(f"The number pulled out was {number}, in which position do you wanna put it (1-5): "))
    number_list[position-1] = number

    number = random.randint(1, x)
    position = int(input(f"The number pulled out was {number}, in which position do you wanna put it (1-5): "))
    number_list[position - 1] = number

    number = random.randint(1, x)
    position = int(input(f"The number pulled out was {number}, in which position do you wanna put it (1-5): "))
    number_list[position - 1] = number

    number = random.randint(1, x)
    position = int(input(f"The number pulled out was {number}, in which position do you wanna put it (1-5): "))
    number_list[position - 1] = number

    number = random.randint(1, x)
    position = int(input(f"The number pulled out was {number}, in which position do you wanna put it (1-5): "))
    number_list[position - 1] = number

    print(number_list)

    if win_game(number_list):
        print("You have won!")

    if not win_game(number_list):
        print("You have lost")

    play_again = input("Do you want to play again (Y/N): ")
    if play_again == "Y":
        game(x)


def win_game(numbers_list):
    if numbers_list[0] <= numbers_list[1] <= numbers_list[2] <= numbers_list[3] <= numbers_list[4]:
        return True


if command == "--game":
    game(25)

if command == "--help":
    print('This is a very simple game; the computer will give you a number, and you must place it form 1 - 5. The '
          'point is to make the numbers be in order :)')
