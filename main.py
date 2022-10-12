#!/usr/bin/env python

# ---------- Typing Test ------------
# Filipe Goncalves, 98083
# Guilherme Cajeira, 93138
# Hugo Hahimoto, 92226

# PSR, October 2022.
# -----------------------------------

import argparse
import readchar
import random
from colorama import Fore, Back, Style
from collections import namedtuple
from time import time, ctime
from pprint import pprint


Input = namedtuple('Input', ['requested', 'received', 'duration'])

INPUTS = []

# Function responsible for calculating statistics
#   Return: Dictionary with game statistics
def Statistics(hits, total, start_game, end_game):
    accuracy = hits / total
    game_duration = end_game - start_game
    average_duration = (sum([dur.duration for dur in INPUTS]) / len(INPUTS)) if len(INPUTS) > 0 else 0
    hit_average_duration = (sum([dur.duration for dur in INPUTS if dur.requested == dur.received]) / hits) if hits > 0 else 0
    miss_average_duration = (sum([dur.duration for dur in INPUTS if dur.requested != dur.received]) / (total-hits)) if (total-hits) > 0 else 0

    statistics = {
        'accuracy': accuracy,
        'inputs': INPUTS,
        'number_of_hits': hits,
        'number_of_types': total,
        'test_duration': game_duration,
        'test_end': ctime(end_game),
        'test_start': ctime(start_game),
        'type_average_duration': average_duration,
        'type_hit_average_duration': hit_average_duration,
        'type_miss_average_duration': miss_average_duration
    }

    return statistics

# Function responsible for realization the game
#   Return: Values needed to calculate statistics
def TypingTest(args):
    # time the start of the game
    start_game = time()

    # number of types and number of successful types
    total = 0
    hits = 0

    while True:
        # get random char from 'a' (ASCII code is 97) to 'z' (ASCII code is 122)
        char_random = chr(random.randint(97, 122))
        print("Type letter: " + Style.BRIGHT + Fore.BLUE + char_random + Style.RESET_ALL)

        # time the game
        time_start_typed = time()
        # read character from user
        char_typed = readchar.readkey()
        # time the game
        time_end_typed = time()

        # calculate time spending since first shown the letter
        char_typed_duration = time_end_typed - time_start_typed
        # total typed keys
        total += 1

        # pressed space key
        if char_typed == ' ':
            print("\nUser pressed " + Style.BRIGHT + Fore.RED + "SPACE" + Style.RESET_ALL + " key - " + Back.RED + Style.BRIGHT + Fore.WHITE + "END GAME" + Style.RESET_ALL)
            break
        
        # append the object to the INPUTS list
        INPUTS.append(Input(char_random, char_typed, char_typed_duration))

        # number of successful inputs
        if char_typed == char_random:
            hits += 1

        print("You typed letter: " + (Style.BRIGHT + Fore.GREEN if char_typed == char_random else Style.BRIGHT + Fore.RED) + char_typed + Style.RESET_ALL)

        # time the possible end of the game
        end_game = time()
        # with time mode True
        if args.use_time_mode == True:
            # check if there is time available
            if end_game - start_game >= args.max_value:
                print("\nCurrent test duration " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(end_game - start_game) + Style.RESET_ALL + " exceeds maximum of " + Style.BRIGHT + Fore.LIGHTBLUE_EX + str(args.max_value) + Style.RESET_ALL) 
                break
        else:
            # check if there are inputs available
            if total >= args.max_value:
                print("\nCurrent test inputs " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(total) + Style.RESET_ALL + " reaches maximum of " + Style.BRIGHT + Fore.LIGHTBLUE_EX + str(args.max_value) + Style.RESET_ALL) 
                break
    
    return Statistics(hits, total, start_game, end_game)


def main():
    # Define argparse inputs:
    #   - use_time_value: TRUE, if the user wants to define the maximum number of seconds
    #                     FALSE, if the user wants to define the maximum number of inputs
    #   - max_value: define maximum number of seconds if use_time_value is TRUE
    #                define maximum number of inputs if use_time_value is FALSE
    parser = argparse.ArgumentParser(description='Definition of ' + Style.BRIGHT + Fore.BLUE + 'test ' +  Style.RESET_ALL + 'mode')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', help='Max number of secs ' + Style.BRIGHT + Fore.RED + 'for time ' +  Style.RESET_ALL + 'mode or maximum number of inputs ' + Style.BRIGHT + Fore.RED + 'for ' +  Style.RESET_ALL + 'number of inputs mode.', required=False)
    parser.add_argument('-mv', '--max_value', type=int, help='Max number of seconds ' + Style.BRIGHT + Fore.RED + 'for time ' +  Style.RESET_ALL + 'mode or maximum number of inputs ' + Style.BRIGHT + Fore.RED + 'for ' +  Style.RESET_ALL + 'number of inputs mode.', required=False)
    args = parser.parse_args()

    # Print args for the user to see the chosen arguments
    print(args)

    # If the arguments are invalid, the test does not start, showing an error message
    if args.max_value == None or args.max_value <= 0:
        print(Back.RED + Style.BRIGHT + Fore.WHITE + "Inputted arguments are invalid!" + Style.RESET_ALL )
        exit(0)

    # Print the game (Typing Test) and the group membres
    print('---------------------------------')
    print('|        ' + Style.BRIGHT + Fore.RED + 'PSR ' + Style.RESET_ALL + 'Typing Test' + '        |')
    print('|                               |')
    print('|            ' + Style.BRIGHT + Fore.BLUE + 'Grupo 3' + Style.RESET_ALL + '            |')
    print('|        Filipe Goncalves       |')
    print('|       Guilherme Cajeira       |')
    print('|         Hugo Hashimoto        |')
    print('---------------------------------\n')

    # Print the type of game the user decided to play
    if args.use_time_mode == False:
        print("Test running up up " + str(args.max_value) + " inputs.")
    else:
        print("Test running up up " + str(args.max_value) + " seconds.")

    # Print the condition to start playing (press any key)
    print("Press " + Back.CYAN + Style.BRIGHT + Fore.WHITE + "any key" + Style.RESET_ALL + " to start the test")
    start_key = readchar.readchar()

    # Call the function responsible for realization the game
    my_dict = TypingTest(args)

    # Print the game is finish
    print(Style.BRIGHT + Fore.YELLOW + "Test Finished!\n" + Style.RESET_ALL)

    # Print game statistics
    pprint(my_dict)



if __name__ == "__main__":
    main()
