# ---constants---
HANGMAN_ASCII_ART = """
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/\n"""

MAX_TRIES = 6
HANGMAN_PHOTOS = {
    0: """    x-------x """,
    1: """\
    x-------x
    |
    |
    |
    |
    |
 """, 2: """\
    x-------x
    |       |
    |       0
    |
    |
    |
 """, 3: """\
    x-------x
    |       |
    |       0
    |       |
    |
    |
 """, 4: """\
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""", 5: """\
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""", 6: """\
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
            """}

# ---variables---
secret_word = ""
old_letters_guessed = []
num_of_tries = 0