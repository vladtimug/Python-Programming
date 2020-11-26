# Hangman Game

# Code Overview
+ The program allows a player to be a part of a Hangman game against the computer.

# Game Features
+ There are 2 modes of playing this game: using hints or without using hints.
+ To access hints the special character '*' must be used as an input.
+ Input values are not case sensitive
+ Display the current state of the words based on all letters guessed
+ Display available letters to guess
+ Display all letters guessed
+ Display number of guesses left
+ Display number of warnings left

# Game Rules
+ Starting Guesses = number of letters in word + 3
+ Warnings per guess = 3
+ Total Score = guesses_remaining * number_unique_letters_in_secret_word
+ The user will only guess one character at a time
+ Only alphabetical characters(letters) are considered as a valid input 
+ If the user inputs anything besides an alphabet (symbols, numbers) he/she loses 1 warning. Whenever a number of 3 warnings have been given a guess is lost. (Warnings will reset to 3 for every guess).
+ If the user inputs a letter that has already been guessed, he/she should lose one warning. If the user has no warnings, they should lose one guess.
+ Consonant Input: If the user inputs a consonant that hasn’t been guessed and the consonant is not in the secret word, the user loses one guess if it’s a consonant.
+ Vowel Input: If the vowel hasn’t been guessed and the vowel is not in the secret word, the user loses two guesses. Vowels are a, e, i, o, and u, y does not count as a vowel.
