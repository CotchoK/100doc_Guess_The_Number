# NUMBER GUESSING GAME

# import language-based functionality
import random as r

# import user defined functions
import ascii_art as aa
import functions as f


def gameloop():
    """
    This is the game play loop that will execute and continue running as long as the user has requested to.
    :return:
    """
    # some ascii art for title
    print(aa.logo)

    # gameplay variables
    number = r.randint(1, 100)  # number the user is to guess
    is_game_over = False  # boolean to control while loop of the game logic
    print(number)

    # define the number of guesses based on difficulty selected
    n_guesses = f.difficulty()

    # I'm thinking of a number between 1 and 100.
    print("I'm thinking of a number between 1 & 100")

    # loop through execution of code until user guesses the number or user runs out of guesses
    while not is_game_over:
        # notify the user of the number of guesses remaining
        print(f"You have {n_guesses} attempts remaining to guess the number.")

        # ask for the user to enter a guessed number
        user_guess = int(input("Make a guess: "))

        # will conduct checking the users guess against the computers and update variables based on outcome
        result, is_game_over, n_guesses = f.compare(user_guess, number, n_guesses)

        # print the text string as a result of the comparison
        print(result)

        # will print Guess Again as long as the game isn't over and that the user still has guesses remaining
        if n_guesses > 1 and not is_game_over:
            print("Guess Again.")

        # will check if the game is over and if so will prompt the user if they want to play again or not.
        if is_game_over:
            response = input("Would you like to play again 'y' or anything else to quit: ")
            if response == 'y':
                f.cls()
                gameloop()
            else:
                exit()


gameloop()
