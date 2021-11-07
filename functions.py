from variables import *

# HANGMAN_ASCII_ART = variables.HANGMAN_ASCII_ART
# MAX_TRIES = variables.MAX_TRIES

# ---functions---


def welcome_title():
    """ print game title """
    print(HANGMAN_ASCII_ART, MAX_TRIES)


def pick_secret_word(file_path, index):
    """ Picking secret word from given file.
    :param file_path: user's file path input
    :param index: user's input number
    :type file_path: str
    :type index: int
    :return: secret word from file
    :rtype: str
    """

    with open(file_path, "r") as my_file:
        words_list = my_file.read().split(" ")
        chosen_word = ""
        if index > len(words_list):
            chosen_word = words_list[index % len(words_list) - 1]
        else:
            chosen_word = words_list[index - 1]
    return chosen_word


def print_uncderscores(secret_word):
    """ printing underscores according to the secret word.
    :param secret_word: the secret word chosen
    :type secret_word: str
    :return: None
    """
    print(len(secret_word) * " _")


def print_hangman(num_of_tries):
    """ printing hangman photo according to number of tries.
    :param num_of_tries: number of tries so far
    :type num_of_tries: int
    :return: None 
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def check_valid_input(letter_guessed, old_letters_guessed):
    """Checking if input is single english letter, newly guessed.
    :param letter_guessed: current letter guessed
    :param old_letters_guessed: old letters guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if input is valid, else false
    :rtype: bool  
    """

    if (len(letter_guessed) > 1 or not(letter_guessed.isalpha()))\
            or letter_guessed in old_letters_guessed:
        result = False
    else:
        result = True
    return result


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Try to update list of old letters guessed with new guess.
    :param letter_guessed: current guessed letter   
    :param old_letters_guessed: old_letters_guessed list 
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: None
    """
    while not check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.sort()
        # ,"Guessed so far: "," -> ".join(old_letters_guessed))
        print("X\n", "Not Valid Input.\n")
        letter_guessed = input("\nGuess a letter: ")

    old_letters_guessed += [letter_guessed.lower()]


def show_hidden_word(secret_word, old_letters_guessed):
    """ Showing the user letters guessed correctly inside
    the secret word underscore structure.

    :param secret_word: the secret word 
    :param old_letters_guessed: old letters guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: None
    """
    my_secret_list = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            my_secret_list.append(letter)
        else:
            my_secret_list.append("_")
    print(" ".join(my_secret_list))


def check_win(secret_word, old_letters_guessed):
    """ Checking if user won, if all letters in secret
    word have been guessed.

    :param secret_word: the secret word
    :param old_letters_guessed: old letters guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: true for win, false for not
    :rtype: bool
    """

    result = True
    for letter in secret_word:
        if letter not in old_letters_guessed:
            result = False
        else:
            continue
    return result


def space_it():
    """ printing blank line. """
    print("\n")
