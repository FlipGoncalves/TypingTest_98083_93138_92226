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


def TypingTest(args):
    start_game = time()
    total = 0
    hits = 0

    while True:
        char_random = chr(random.randint(97, 122))
        print("Type letter: " + Style.BRIGHT + Fore.BLUE + char_random + Style.RESET_ALL)

        time_start_typed = time()
        char_typed = readchar.readkey()
        time_end_typed = time()
        char_typed_duration = time_end_typed - time_start_typed
        total += 1

        if char_typed == ' ':
            print("\nUser pressed " + Style.BRIGHT + Fore.RED + "SPACE" + Style.RESET_ALL + " key - " + Back.RED + Style.BRIGHT + Fore.WHITE + "END GAME" + Style.RESET_ALL)
            break
        else:
            INPUTS.append(Input(char_random, char_typed, char_typed_duration))

        if char_typed == char_random:
            hits += 1

        print("You typed letter: " + (Style.BRIGHT + Fore.GREEN if char_typed == char_random else Style.BRIGHT + Fore.RED) + char_typed + Style.RESET_ALL)

        end_game = time()
        if args.use_time_mode == True:
            if end_game - start_game >= args.max_value:
                print("\nCurrent test duration " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(end_game - start_game) + Style.RESET_ALL + " exceeds maximum of " + Style.BRIGHT + Fore.LIGHTBLUE_EX + str(args.max_value) + Style.RESET_ALL) 
                break
        else:
            if total >= args.max_value:
                print("\nCurrent test inputs " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(total) + Style.RESET_ALL + " reaches maximum of " + Style.BRIGHT + Fore.LIGHTBLUE_EX + str(args.max_value) + Style.RESET_ALL) 
                break
    
    return Statistics(hits, total, start_game, end_game)


def main():
    parser = argparse.ArgumentParser(description='Definition of ' + Style.BRIGHT + Fore.BLUE + 'test ' +  Style.RESET_ALL + 'mode')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', help='Max number of secs ' + Style.BRIGHT + Fore.RED + 'for time ' +  Style.RESET_ALL + 'mode or maximum number of inputs ' + Style.BRIGHT + Fore.RED + 'for ' +  Style.RESET_ALL + 'number of inputs mode.', required=False)
    parser.add_argument('-mv', '--max_value', type=int, help='Max number of seconds ' + Style.BRIGHT + Fore.RED + 'for time ' +  Style.RESET_ALL + 'mode or maximum number of inputs ' + Style.BRIGHT + Fore.RED + 'for ' +  Style.RESET_ALL + 'number of inputs mode.', required=False)
    args = parser.parse_args()
    print(args)

    if args.max_value == None or args.max_value <= 0:
        print(Back.RED + Style.BRIGHT + Fore.WHITE + "Inputted arguments are invalid!" + Style.RESET_ALL )
        exit(0)

    print('---------------------------------')
    print('|        ' + Style.BRIGHT + Fore.RED + 'PSR ' + Style.RESET_ALL + 'Typing Test' + '        |')
    print('|                               |')
    print('|            ' + Style.BRIGHT + Fore.BLUE + 'Grupo 3' + Style.RESET_ALL + '            |')
    print('|        Filipe Goncalves       |')
    print('|       Guilherme Cajeira       |')
    print('|         Hugo Hashimoto        |')
    print('---------------------------------\n')

    if args.use_time_mode == False:
        print("Test running up up " + str(args.max_value) + " inputs.")
    else:
        print("Test running up up " + str(args.max_value) + " seconds.")

    print("Press " + Back.CYAN + Style.BRIGHT + Fore.WHITE + "any key" + Style.RESET_ALL + " to start the test")
    start_key = readchar.readchar()

    my_dict = TypingTest(args)

    print(Style.BRIGHT + Fore.YELLOW + "Test Finished!\n" + Style.RESET_ALL)

    pprint(my_dict)



if __name__ == "__main__":
    main()
