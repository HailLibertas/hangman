import random


# Fill up the variables
import sys

lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
wordlist = ['python', 'java', 'swift', 'javascript']
chosen_word = random.choice(wordlist)
guessed_letters = list()
hidden = '-' * len(chosen_word)
all_guessed_letters = list()
comp_tally = int()
player_tally = int()
attempts_counter = 8


def contains(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        found = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            return True

    return False


def check_input(n):

    if len(n) != 1:
        print("Please, input a single letter")
    elif not contains(lower_alphabet, n):
        print("Please, enter a lowercase letter from the English alphabet.")
    elif not contains(chosen_word, n) and len(n) == 1 and n not in all_guessed_letters and n not in guessed_letters:
        print("That letter doesn't appear in the word")
        global attempts_counter
        attempts_counter -= 1
        all_guessed_letters.append(n)
        guessed_letters.append(n)
    elif n in all_guessed_letters and n in guessed_letters and len(n) == 1:
        print("You've already guessed this letter.")


def game():
    global hidden, chosen_word, player_tally, comp_tally, attempts_counter, all_guessed_letters, guessed_letters, chosen_word

    while attempts_counter > 0:
        print("\n" + hidden)
        guess = input("Input a letter: ")
        check_input(guess)

        if guess in chosen_word:
            for index in range(len(chosen_word)):
                if guess == chosen_word[index]:
                    hidden = hidden[:index] + guess + hidden[index + 1:]
            all_guessed_letters.append(guess)
            guessed_letters.append(guess)
        if hidden == chosen_word:
            print(f"You guessed the word {hidden}!")
            print("You survived!")
            player_tally += 1
            chosen_word = random.choice(wordlist)
            hidden = '-' * len(chosen_word)
            guessed_letters.clear()
            all_guessed_letters.clear()
            looper()
            return
    else:
        print("You lost!")
        comp_tally = comp_tally + 1
        chosen_word = random.choice(wordlist)
        hidden = '-' * len(chosen_word)
        guessed_letters.clear()
        all_guessed_letters.clear()
        looper()
        return


print("H A N G M A N")


def looper():
    menu = input("""
            Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:
            """)
    if menu == 'play':
        game()

    elif menu == 'results':
        print(f"You won: {player_tally} times\n"
              f"You lost: {comp_tally} times")
        looper()
    elif menu == 'exit':
        return
    else:
        looper()


looper()
