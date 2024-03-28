import math
import random


#bellow is the Helper function to take guesses that only contain alphabets and has a overall lenght of 5.
def get_player_guess():
    guess = input("Please enter your guess: ")
    while len(guess) != 5 or guess.isalpha() == False:
        guess = input("Your guess must have 5 letters: ")
    return guess.lower()

#Helper function to update the letters in game_state.
def letter_updator(word, guess, game_state):
    game_state = ["_"] * 5
    for i in range(0,5):
        if guess[i] == word[i]:
            game_state[i] = word[i].upper()
        else:
            game_state[i] = "_"
    for i in range(0,5):
        if guess[i] in word:
            if guess[i] != word[i]:
               game_state[i] = guess[i].lower()
            if game_state.count(guess[i]) + game_state.count(guess[i].upper()) > word.count(guess[i]):
                if game_state[i] == guess[i]:
                    game_state[i] = "_"
    return game_state

#Helper function to check if the game was won, or the player ran out of time. 
#Then returning a tuple with the amount of gueses taken and whether they won or not.
def win_checker(guess_counter):
    is_solved = False
    if guess_counter < 7:
        is_solved = True
    return (guess_counter, is_solved)


#Below contains Helper function to check game_state and if the guess is corect it will print the game_state
def play_round(word):
    game_state = ["_","_","_","_","_"]
    guess_counter = 0
    while "".join(game_state).lower() != word and guess_counter < 7:
        guess_counter += 1
        if guess_counter > 6:
            return win_checker(guess_counter)
        print(f"Guess {guess_counter}:" + "\n")
        guess = get_player_guess()
        game_state = letter_updator(word, guess, game_state)
        print(" ".join(game_state) + "\n")
    return win_checker(guess_counter)
    

#Helper function to check whether the player wants to play again, checks to see if the answer is 'Y' or 'N' only.
def  yes_or_no(playing_status):
    playing_status = input("Please enter 'Y' to continue or 'N' to stop playing: ")
    while playing_status != "Y" and playing_status != "N":
        print("Only enter 'Y' or 'N'!")
        playing_status = input("Please enter 'Y' to continue or 'N' to stop playing: ")
    return playing_status

#Helper function to print the rules of the game and do a little greetings to the player using their name. 
def get_rules():
    name = input("Please enter your name: ")
    print("\n" + f"Welcome to Wordle 101 {name}" + "\n")
    print("=" * 72)
    print(" " * 33 + "Rules" + " " * 39)
    print("You have 6 guesses to figure out the solution." + "\n" + "All solutions are words that are 5 letters long.")
    print("Words may include repeated letters.")
    print("Letters that have been guessed correctly are displayed in uppercase." + "\n" + "Letters that are in the word but have been guessed in the wrong location")
    print("are displayed in lowercase.")
    print("=" * 72 + "\n" * 2)


#Below contains Helper function to print the instruction for this wordle game, then to start the wordle game. 
def play_game(word, word_list):
    round = 0
    round_won = 0
    playing_status = ""
    guess_dict = {1:0,2:0,3:0,4:0,5:0,6:0}
    get_rules()
    while playing_status != "N":
        round += 1
        print(f"Round: {round}" + "\n")
        guess_counter, is_solved = play_round(word)
        if is_solved == True:
            print(f"Success! The word is {word}!" + "\n")
            round_won += 1
            guess_dict[guess_counter] += 1
        elif is_solved == False:
            print(f"Better luck next time! The word is {word}!" + "\n")
        playing_status = yes_or_no(playing_status)
        print()
        word = get_random_word(word_list)
    if_player_quits(round, round_won, guess_dict)

#Helper function to open file, then take the words in the file to create a list, while ignoring the empty spaces.
def get_words(filename):
    open_file = open(filename, "r")
    word_list = open_file.read().split()
    open_file.close()
    return(word_list)

#Helper function to print a bar chart, by taking a dictionary after sorting it based on the keys.
def print_bar_chart(data_dict):
    keys_list = []
    for keys in data_dict.keys():
        keys_list.append(keys)
    
    keys_list.sort()
    for keys in keys_list:
        print(str(keys) + "|" + "#" * data_dict[keys] + str(data_dict[keys]))

#Helper function to print the wall of sumary of the game after the player quits playing. 
def if_player_quits(round, round_won, guess_dict):
    print("=" * 72 + "\n" + " " * 32 + "Summary" + " " * 40)
    win_rate = round_won/round * 100
    win_rate = math.ceil(win_rate)
    print(f"Win percentage: {int(win_rate)}%")
    print("Win Distribution:")
    print_bar_chart(guess_dict)
    print("=" * 72)


#Helper Function to get filename
def get_filename():
    filename = input("Enter the name of the word file(include full name, e.g WordFile1.txt): ")
    return filename

#Helper function to call random words from wordlist
def get_random_word(word_list):
    word = random.choice(word_list)
    return word
#main function that calls the helper functions that makes this "program" posible!
def main():
    filename = get_filename()
    word_list = get_words(filename)
    word = get_random_word(word_list)
    play_game(word, word_list)


main()
