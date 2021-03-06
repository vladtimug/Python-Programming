# Screabble Game
# ----------------------

import math
import random
import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

        The score for a word is the product of two components:

        The first component is the sum of the points for letters in the word.
        The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

        Letters are scored as in Scrabble; A is worth 1, B is
        worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    component1 = 0
    for char in word.lower():
        for index, letter in enumerate(SCRABBLE_LETTER_VALUES.keys()):
            if letter == char:
                letter_points = SCRABBLE_LETTER_VALUES[letter]
                component1 += letter_points
    component2 = max(7 * len(word) - 3 * (n - len(word)), 1)
    score = component1 * component2
    return score

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")  # print all on the same line
    print()  # print an empty line

    
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3))
    wildcard_pos = random.choice(range(num_vowels))
    for i in range(num_vowels):
        if i == wildcard_pos:
            x = "*"
            hand[x] = hand.get(x, 0) + 1
        else:
            x = random.choice(VOWELS)
            hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # print("Hand:", hand)
    word = word.lower()
    # print("word:", word)
    freq = 0
    updated_hand = hand.copy()
    for letter in hand:
        # print("Current letter:", letter)
        if letter in word:
            # print("\tLetter in word")
            freq = word.count(letter)
            # print("\tLetter freq:", freq)
        else:
            freq = 0
            # print("\tLetter freq:", freq)

        updated_hand[letter] -= freq

        # Remove entry if freq is 0
        if updated_hand[letter] == 0:
            del updated_hand[letter]

    return updated_hand


def listToString(s):
    """
    Returns a string of non-spaced elements
    Input -> list
    Output -> string
    """
    str1 = ""
    return str1.join(s)


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    present = False
    hand_letters_list = []
    # Create a list with all the letters in hand
    for element in hand.keys():
        for frequency in range(hand[element]):
            hand_letters_list.append(
                element
            )  

    # Compute the total number of letters available in hand
    hand_letters_total = sum(
        list(hand.values())
    ) 

    verified = 0
    if word in word_list:
        verified = 0
        # Check if all letters in word are found in hand
        if all(element in hand_letters_list for element in list(word)):
            for letter in word:
                if word.count(letter) <= hand[letter]:
                    verified += 1
                else:
                    verified -= 1
    else:
        listed_word = list(word)
        if "*" in listed_word:
            if all(element in hand_letters_list for element in listed_word):
                wild_card_pos = listed_word.index("*")
                prefix = listed_word[:wild_card_pos]
                sufix = listed_word[wild_card_pos + 1 :]
                for vowel in VOWELS:
                    new_word = listToString(prefix) + vowel + listToString(sufix)
                    if new_word in word_list:
                        present = True
                listed_word.remove("*")

    if verified == len(word):
        present = True
    return present


def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    return len(list(hand.keys()))


def listToStringSpaced(s):
    """
    Returns a string of spaced elements
    Input -> list
    Output -> string
    """
    str1 = " "
    return str1.join(s)


def listed_hand(hand):
    """
    Returns a string containing all available letters in the current hand
    * Input -> dictionary
    * Output -> string

    """
    hand_letters_list = []
    for element in hand.keys():
        for frequency in range(hand[element]):
            hand_letters_list.append(element)

    return listToStringSpaced(hand_letters_list)


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    letters_left = len(list(hand.keys()))
    hand_length = letters_left
    total_score = 0
    while letters_left > 0:
        print("Current hand:", listed_hand(hand))
        current_word = input("Enter word, or '!!' to indicate that you are finished: ")
        if current_word == "!!":
            print("Total score:", total_score)
            print()
            break
        elif is_valid_word(current_word, hand, word_list):
            hand = update_hand(hand, current_word)
            total_score += get_word_score(current_word, hand_length)
            print(
                '"' + current_word + '" has earned',
                get_word_score(current_word, hand_length),
                "points. Total score is:",
                total_score,
            )
            print()
            letters_left -= len(current_word)
            if letters_left == 0:
                print("Ran out of letters.")
                print()
        else:
            print("That is not a valid word. Please choose another word")
            print()
            hand = update_hand(hand, current_word)
            letters_left -= len(current_word)
            if letters_left == 0:
                print("Ran out of letters.")
    
    return total_score

#
# procedure you will use to substitute a letter in a hand
#


def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    # Generate substitute letter and confirm its existing conditions
    substitute_letter = random.choice(VOWELS + CONSONANTS)
    while substitute_letter in list(hand) and substitute_letter == letter:
        substitute_letter = random.choice(VOWELS + CONSONANTS)
    print("Substitute is:", substitute_letter)

    updated_hand = hand.copy()

    # Replace the letter in the updated_hand
    if letter in list(hand):
        print("Found letter", letter, "in hand", hand)
        del updated_hand[letter]
        updated_hand[substitute_letter] = 1

    return updated_hand


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    total_score = 0
    no_of_hands = eval(input("Enter total number of hands: "))
    while no_of_hands > 0:
        current_hand = deal_hand(HAND_SIZE)
        print("Current hand: ", listed_hand(current_hand))
        
        # Handle the substitution of a letter
        while True:
            substitutes = input("Would you like to substitute one letter from your hand? yes/no, y/n: ")
            if substitutes == 'yes' or substitutes == 'y' or substitutes == 'Y':
                letter_to_replace = input("Type in the letter from your hand to change: ")
                current_hand = substitute_hand(current_hand, letter_to_replace)
                print()
                break
            elif substitutes == 'no' or substitutes == 'n' or substitutes == 'N':
                print("No substitution.")
                print()
                break
            else:
                print("Please enter a valid answer")
                print()
        
        total_score += play_hand(current_hand, word_list)
        no_of_hands -= 1
    
    return total_score

if __name__ == "__main__":
    word_list = load_words()
    print("----------------------------------------------------------------------")
    print()
    # play_hand(deal_hand(HAND_SIZE), word_list)
    play_game(word_list)
