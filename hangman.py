import random

def hangman(word):
    wrong = 0                                   # variable to keep track of wrong guesses
    stages =    ["",                            # draws the picture for each wrong guess
                "______     ",
                "|     |    ",
                "|     |    ",
                "|     0    ",
                "|    /|\   ",
                "|    / \   ",
                "|          ",
                "|__________",
                ""]
    remaining_letters = list(word)              # variable keeps a list of the letters in the word
    board = ["_"] * len(word)                   # the board will be a list of underscores for each character of the word
    win = False                                 # Boolean to check if game is won
    print("Welcome to Hangman")                 #intro
    while wrong < len(stages) - 1:                  # loop to keep the game going until more wrong guesses than the picture
        print("")
        msg = "Guess a letter: "
        char = input(msg)
        if char in remaining_letters:                   # creates a loop to reveal all cases of guessed letter, not just the first one
            while char in remaining_letters:            # players guess saved in the char
                cind = remaining_letters.index(char)    # is the guess in the list of letters from the word?
                board[cind] = char                      # update board using the matching index
                remaining_letters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))                    # prints the board with correctly guessed letter shown
        e = wrong + 1
        print("\n".join(stages[: e]))               # prints the stages
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! it was '{}'.".format(word))

def randomWord(words):                              # function to randomly pick a letter from the list of words below
    index = random.randint(0, len(words))
    return words[index]

words = 'ant babboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole rat raven rhino shark sheep spider toad turkey turtle wolf wombat zebra'
word = randomWord(words.split())

hangman(word)