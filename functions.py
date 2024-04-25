import os  # used to import the clear screen functionality


# define the clear terminal screen function
# note ensure to check the Emulate Terminal in Output Console in the Configurations settings
def cls():
    """
    Clears the console screen (ensure to enable Emulate Terminal in Output Console in Pycharm's Config settings)
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def compare(guess, num):
    """
    Conducts a comparison between the user's guess and the number selected by the computer
    :param guess: the user's guess passed as a parameter
    :param num: the computer selected number the user is attempting to guess
    :return: string that will be used in conjunction with a dictionary including those options for outputs
    """
    if guess == num:
        return "win"
    elif guess > num:
        return "higher"
    else:
        return "lower"

