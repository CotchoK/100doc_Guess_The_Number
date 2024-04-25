import os  # used to import the clear screen functionality


# define the clear terminal screen function
# note ensure to check the Emulate Terminal in Output Console in the Configurations settings
def cls():
    """
    Clears the console screen (ensure to enable Emulate Terminal in Output Console in Pycharm's Config settings)
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def compare(guess, num, lives):
    """
    Conducts a comparison between the user's guess and the number selected by the computer
    :param guess: the user's guess passed as a parameter
    :param num: the computer selected number the user is attempting to guess
    :param lives: the number of guesses/lives the player has remaining
    :return: a string based on the result of the comparison check
            ,boolean to update game loop
            ,number of guesses remaining
    """

    # these are preset responses base on comparison conditions (could hard code in return statements but experimenting
    # with dictionaries)
    response = {
        "win": "You win",
        "higher": "Too High",
        "lower": "Too Low",
        "lose": "You have run out of guesses. You lose",
    }

    if lives > 1:
        if guess == num:
            return response['win'], True, lives
        else:
            lives -= 1
            if guess > num:
                return response["higher"], False, lives
            elif guess < num:
                return response["lower"], False, lives
    else:
        return response["lose"], True, lives

def difficulty():
    """
    Asks the user to enter the difficulty they want to play the game
    :return: difficulty level of the game
    """
    mode = ''
    # loop until user provides valid response to difficulty selection
    while mode != 'easy' and mode != 'hard':

        mode = input("Please enter either 'easy' or 'hard' for difficulty: ")

        # user selects difficulty
        if mode == 'easy':
            return 10
        elif mode == 'hard':
            return 5