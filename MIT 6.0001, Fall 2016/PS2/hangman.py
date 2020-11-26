# Hangman Game
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """

    checked = len(secret_word)

    for guess in letters_guessed:
        if guess in secret_word:
            checked -= secret_word.count(guess)

    if checked == 0:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
   
    word_copy_dash = ""
    for pos in range(len(secret_word)):
        word_copy_dash += "_ "
    for letter in range(len(secret_word)):
        for guess in letters_guessed:
            if secret_word[letter] == guess:
                word_copy_dash = (
                    word_copy_dash[: letter * 2]
                    + guess
                    + word_copy_dash[letter * 2 + 1 :]
                )
    return word_copy_dash


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    
    res = string.ascii_lowercase
    for letter in letters_guessed:
        if letter in string.ascii_lowercase:
            res = res.replace(letter, "")
    return res


def unique_letters(secret_word):
    """
    *secret_word: string, the secret word to be guessed
    *returns: uniques, int, number of unique letters in secret_word
    """
    
    uniques = 0
    for char in list(secret_word):
        if secret_word.count(char) == 1:
            uniques += 1

    return uniques


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    
    print()
    print("\nI am thinking of a word that is {} letters long.".format(len(secret_word)))
    print(secret_word)
    guesses = len(secret_word) + 3
    guesses_copy = guesses
    guessed = False
    print("Starting guesses: ", guesses)
    no_warnings = False
    letters_guessed = []
    vowels = ["a", "e", "i", "o"]
    while guesses > 0:
        warnings = 3
        warning_check = False  # True when value of warnings reaches 0
        print("Warnings left: ", warnings)
        print("---------------")
        if (
            guesses == guesses_copy and len(letters_guessed) == 0
        ):  # First guess behaviour
            # print("IF 1")
            reset = False  # True when value of warnings resets from 0 to 3
            guess = input("\nLetter to guess: ").lower()
            while not guess.isalpha():  # Handle non letter inputs
                # print("WHILE 1")
                print("Your input was not a letter. Try again!")
                if not warning_check or reset:
                    warnings -= 1
                else:
                    warnings = 3
                    reset = True
                print("Warnings left: ", warnings)
                print("---------------")
                guess = input("\nLetter to guess: ").lower()
                if warnings == 0:  # Guesses reset
                    guesses -= 1
                    print("You lost one guess.")
                    print("Guesses left: ", guesses)
                    warning_check = True
                    reset = False
                    first_guess = False
            if guess in vowels and guess not in secret_word:
                guesses -= 2
            elif guess not in vowels and guess not in secret_word:
                guesses -= 1
            letters_guessed.append(guess)
            first_guess = True
        elif (
            guesses < guesses_copy and first_guess == False or len(letters_guessed) >= 1
        ):
            # print("IF 2")
            guess = input("\nLetter to guess: ").lower()
            if guess in letters_guessed:
                # print("IF 3 - guesss in letters-guessed")
                while guess in letters_guessed:
                    # print("WHILE 2 - guess in letters-guessed")
                    print("You already guessed this letter. Try another one!")
                    warnings -= 1
                    print("Warnings left: ", warnings)
                    print("---------------")
                    if warnings == 0:
                        guesses -= 1
                        print("You lost one guess.")
                        print("Guesses left: ", guesses)
                        warnings = 4
                    guess = input("\nLetter to guess: ").lower()
            # else:
            while not guess.isalpha():
                # print("WHILE 3 - guess not letter")
                warnings -= 1
                print("Your input was not a letter. Try again!")
                print("Warnings left: ", warnings)
                print("---------------")
                guess = input("\nLetter to guess: ").lower()
                if warnings == 0:
                    guesses -= 1
                    print("You lost one guess.")
                    print("Guesses left: ", guesses)
                    warnings = 4

            if guess in vowels and guess not in secret_word:
                guesses -= 2
            elif guess not in vowels and guess not in secret_word:
                guesses -= 1
            letters_guessed.append(guess)
        if len(letters_guessed) == 1:
            first_guess = False
        print("Current status: ", get_guessed_word(secret_word, letters_guessed))
        print("Available letters: ", get_available_letters(letters_guessed))
        print("Guesses left:", guesses)
        print("Letters guessed", letters_guessed)
        if is_word_guessed(secret_word, letters_guessed):
            if guesses != guesses_copy:
                guesses_left = guesses_copy - guesses
            else:
                guesses_left = guesses
            total_score = guesses_left * unique_letters(secret_word)
            print("\n---------------")
            print("Congratulations, you won!")
            print("Your total score for this game is:", total_score)
            break
        elif not is_word_guessed(secret_word, letters_guessed) and guesses == 0:
            print("\nOops, you lost. You should try again.")
            print("The secret word is: ", secret_word)
            break
        elif no_warnings:
            print("\nOops, you lost. You should try again.")
            print("The secret word is: ", secret_word)
            break


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    
    my_word_list = my_word.split()
    pos1 = list(enumerate(my_word_list))
    pos2 = list(enumerate(other_word))
    checked = 0
    guessed = [
        letter for letter in my_word_list if letter.isalpha()
    ]  # extract all letters in my_word
    if len(my_word.split()) == len(other_word):
        for i in list(
            zip(pos1, pos2)
        ):  # separate and extract corresponding elements in a list
            if i[0][1] == i[1][1]:  # compare letters in corresponding possitions
                checked += 1
            elif i[0][1] == "_":
                checked += 1
        if checked == len(other_word) and not all(
            elem in guessed for elem in list(other_word)
        ):
            return True
        else:
            return False
    else:
        return False


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """

    my_word = my_word.split()
    no_space_word = ""
    no_space_word = no_space_word.join(my_word)
    pos = []
    mask = []
    freq = []
    position = -1
    for char in no_space_word:  # extract all the positions of characters
        if char.isalpha():  # and the characters that are letters
            position += 1  # for <my_word>
            pos.append(position)
            mask.append(char)
        else:
            position += 1
    freq1 = {
        i: no_space_word.count(i) for i in set(no_space_word)
    }  # extract ferquency of each literal char in my_word
    del freq1["_"]  # and delete the dash key
    for word in wordlist:  # for every word in the list
        if len(word) == len(no_space_word):  # filter by length of <my_word>
            count = 0  # and print only the matching words
            out = False
            for index in range(len(word)):
                for value in pos:
                    if index == value and word[index] == no_space_word[value]:
                        count += 1
            for char in word:
                if char in freq1:
                    if freq1.get(char) != word.count(
                        char
                    ):  # compare frequency of each char found in my_word with the frequency of each char in word
                        out = True  # out = True if the 2 frequencies are different
            if count == len(pos) and not out:
                print(word, end=", ")


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print()
    print("\nI am thinking of a word that is {} letters long.".format(len(secret_word)))
    print(secret_word)
    guesses = len(secret_word) + 3
    guesses_copy = guesses
    guessed = False
    print("Starting guesses: ", guesses)
    no_warnings = False
    letters_guessed = []
    vowels = ["a", "e", "i", "o"]
    while guesses > 0:
        warnings = 3
        warning_check = False  # True when value of warnings reaches 0
        print("Warnings left: ", warnings)
        print("---------------")
        if (
            guesses == guesses_copy and len(letters_guessed) == 0
        ):  # First guess behaviour
            # print("IF 1")
            reset = False  # True when value of warnings resets from 0 to 3
            guess = input("\nLetter to guess: ").lower()
            while not guess.isalpha():  # Handle non letter inputs
                # print("WHILE 1")
                if guess == "*":
                    print("Guess at least one letter to get hints.")
                print("Your input was not a letter. Try again!")
                if (not warning_check or reset) and guess != "*":
                    warnings -= 1
                else:
                    warnings = 3
                    reset = True
                print("Warnings left: ", warnings)
                print("---------------")
                guess = input("\nLetter to guess: ").lower()
                if warnings == 0:  # Guesses reset
                    guesses -= 1
                    print("You lost one guess.")
                    print("Guesses left: ", guesses)
                    warning_check = True
                    reset = False
                    first_guess = False
            if guess in vowels and guess not in secret_word and guess != "*":
                guesses -= 2
            elif guess not in vowels and guess not in secret_word and guess != "*":
                guesses -= 1
            letters_guessed.append(guess)
            first_guess = True
        elif (
            guesses < guesses_copy and first_guess == False or len(letters_guessed) >= 1
        ):
            # print("IF 2")
            guess = input("\nLetter to guess: ").lower()
            if guess == "*":
                print("Possible word matches are: ")
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            elif guess in letters_guessed:
                # print("IF 3 - guesss in letters-guessed")
                while guess in letters_guessed:
                    # print("WHILE 2 - guess in letters-guessed")
                    print("You already guessed this letter. Try another one!")
                    warnings -= 1
                    print("Warnings left: ", warnings)
                    print("---------------")
                    if warnings == 0:
                        guesses -= 1
                        print("You lost one guess.")
                        print("Guesses left: ", guesses)
                        warnings = 4
                    guess = input("\nLetter to guess: ").lower()
            # else:
            while not guess.isalpha() and not "*":
                # print("WHILE 3 - guess not letter")
                warnings -= 1
                print("Your input was not a letter. Try again!")
                print("Warnings left: ", warnings)
                print("---------------")
                guess = input("\nLetter to guess: ").lower()
                if warnings == 0:
                    guesses -= 1
                    print("You lost one guess.")
                    print("Guesses left: ", guesses)
                    warnings = 4

            if guess in vowels and guess not in secret_word and guess != "*":
                guesses -= 2
            elif guess not in vowels and guess not in secret_word and guess != "*":
                guesses -= 1
            if guess != "*":
                letters_guessed.append(guess)
        if len(letters_guessed) == 1:
            first_guess = False
        print("\nCurrent status: ", get_guessed_word(secret_word, letters_guessed))
        print("Available letters: ", get_available_letters(letters_guessed))
        print("Guesses left:", guesses)
        print("Letters guessed", letters_guessed)
        if is_word_guessed(secret_word, letters_guessed):
            if guesses != guesses_copy:
                guesses_left = guesses_copy - guesses
            else:
                guesses_left = guesses
            total_score = guesses_left * unique_letters(secret_word)
            print("\n---------------")
            print("Congratulations, you won!")
            print("Your total score for this game is:", total_score)
            break
        elif not is_word_guessed(secret_word, letters_guessed) and guesses == 0:
            print("\nOops, you lost. You should try again.")
            print("The secret word is: ", secret_word)
            break
        elif no_warnings:
            print("\nOops, you lost. You should try again.")
            print("The secret word is: ", secret_word)
            break


if __name__ == "__main__":

    hints = input("Would you like to play the game with hints? y/n: ")

    if hints == "n" or hints == "no":
        secret_word = choose_word(wordlist)
        hangman(secret_word)
    elif hints == "y" or hints == "yes":
        secret_word = choose_word(wordlist)
        print("Insert the symbol * to see the hints for the current guess.")
        hangman_with_hints(secret_word)
    else:
        print("Please answer with yes(y) or no(n).")
        while hints != "n" or hints != "no" or hints != "y" or hints != "yes":
            hints = input("\nWould you like to play the game with hints? y/n: ")
            if hints == "n" or hints == "no":
                secret_word = choose_word(wordlist)
                hangman(secret_word)
                break
            elif hints == "y" or hints == "yes":
                secret_word = choose_word(wordlist)
                print("Insert the symbol * to see the hints for the current guess.")
                hangman_with_hints(secret_word)
                break
            else:
                print("Please answer with yes(y) or no(n).")