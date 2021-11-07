from variables import *
from functions import *

def main():
    global num_of_tries
    #---the program---
    welcome_title()
    space_it()

    file_path = (input("Enter file path: \n(Leave empty for default file)\n")).strip() or "./hangman-words.txt"
    index = int(input("Enter index: \n(will be used to pick a word from the file)\n"))
    secret_word = pick_secret_word(file_path, index)
    space_it()

    print("Let's start!")
    space_it()

    print_hangman(num_of_tries)
    print_uncderscores(secret_word)

    while num_of_tries < 6:
        letter_guessed = input("\nGuess a letter: ")
        try_update_letter_guessed(letter_guessed, old_letters_guessed)

        if old_letters_guessed[-1] not in secret_word: # wrong guess
            num_of_tries += 1
            print("\n:( Wrong Guess...\n")
            # space_it()
            print_hangman(num_of_tries)

        show_hidden_word(secret_word, old_letters_guessed)

        print("\n(Guessed so far: "," -> ".join(old_letters_guessed),")\n")


        if check_win(secret_word, old_letters_guessed): 
            print("WIN")
            break
    
    if not check_win(secret_word, old_letters_guessed):
        print("LOSE")
    input() # ment for window to stay open until hit enter.
        

if __name__ == "__main__":
    main()