import random


# You guess the random number
def main(x):
    random_number = random.randint(1, x)
    number = 0
    while number != random_number:
        number = int(input(f"Guess a number between 1 and {x}: "))
        if number > random_number:
            print("Too high :(")
        elif number < random_number:
            print("Too low :(")
    print(f"Great you guesses de number {x}")
    play_again = input("Wanna play again? (Y/N) ")
    if play_again == "Y":
        main(x)


# main(10)

# You try to get the computer to guess the random number
def computer_guess(y):
    global guess
    low = 1
    high = y
    feedback = ""
    while feedback != "correct":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} to high (H), too low (L), or correct(correct) ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"The number guessed was {guess}")
    play_again = input("Do you wanna play again? (Y/N)")
    if play_again == "Y":
        computer_guess(y)

# computer_guess(150)

# Rock Paper Scissors
def play():
    user = input("Rock, Paper or Scissors? ")
    game = random.choice(["Rock", "Paper", "Scissors"])
    if user == game:
        print('You tied')

    elif win(user, game):
        print('You win')

    elif not win(user, game):
        print('You lost')

    play_again = input("Do you wanna play again?(Y/N) ")
    if play_again == "Y":
        play()

def win(player, opponent):
    if (player == "Rock" and opponent == "Scissors") or (player == "Scissors" and opponent == "Paper") or \
    (player == "Paper" and opponent == "Rock"):
        return True

# play()


