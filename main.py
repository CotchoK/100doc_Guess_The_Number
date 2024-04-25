# NUMBER GUESSING GAME

# import language-based functionality
import random as r

# import user defined functions
import ascii_art as aa
import functions as f


def gameloop():
    """
    This is the game play loop that will excute and continue running as long as the user has requested to.
    :return:
    """
    # some ascii art for title
    print(aa.logo)

    # gameplay variables
    number = r.randint(1, 100)  # number the user is to guess
    mode = ''  # mode variable to store difficulty selection
    n_guesses = 0  # number of guess variable that initialises to 0
    is_game_over = False  # boolean to control while loop of the game logic
    responses = {
        "win": "You win",
        "higher": "Too High",
        "lower": "Too Low",
    }
    # print(number)

    # loop until user provides valid response to difficulty selection
    while mode != 'easy' and mode != 'hard':
        # user selects difficulty
        mode = input("Please enter either 'easy' or 'hard' for difficulty: ")

        if mode == 'easy':
            n_guesses = 10
        elif mode == 'hard':
            n_guesses = 5

    # I'm thinking of a number between 1 and 100.
    print("I'm thinking of a number between 1 & 100")

    # loop through execution of code until user guesses the number or user runs out of guesses
    while not is_game_over:
        # notify the user of the number of guesses remaining
        if n_guesses == 0:
            print(f"You have run out of guesses. You lose")
            is_game_over = True
        else:
            print(f"You have {n_guesses} attempts remaining to guess the number.")

        # ask for the user to enter a guessed number
        user_guess = int(input("Make a guess: "))

        result = f.compare(user_guess, number)
        print(responses[result])
        if result == 'win':
            is_game_over = True
        else:
            n_guesses -= 1
            if n_guesses == 0:
                print(f"You have run out of guesses. You lose")
                is_game_over = True
            else:
                print("Guess Again.")

        if is_game_over:
            response = input("Would you like to play again 'y' or anything else to quit: ")
            if response == 'y':
                f.cls()
                gameloop()
            else:
                exit()


gameloop()
