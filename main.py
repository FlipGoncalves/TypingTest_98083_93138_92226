#!/usr/bin/env python
# --------------------------------------------------
# Typing Test
# Filipe Goncalves, 98083
# Hugo Hahimoto, 92226
# Guilherme Cajeira, 93138
# PSR, October 2022.
# --------------------------------------------------

import readchar
from pprint import pprint
import argparse
from colorama import Fore, Style
from collections import namedtuple
import random
import time

Input = namedtuple('KeyInput', ['requested', 'received', 'duration'])

INPUTS = []

def playGame(args):

    # start the game
    game_start = time.time()
    count = 0
    right_hits = 0

    # loop
    while True:

        # character between a (97 in ASCII) and z (122 in ASCII)
        character = chr(random.randint(97, 122))
        print("Type letter: " + Fore.CYAN + character + Style.RESET_ALL)
        
        # get received key
        time_start = time.time()
        k = readchar.readkey()
        time_end = time.time()
        count += 1

        INPUTS.append(Input(character, k, time_end-time_start))

        end_game = time.time()

        # if key is space
        if k == ' ':
            print("\nUser pressed SPACE key - END GAME")
            break

        print("You typed letter: " + (Fore.GREEN if k == character else Fore.RED) + k + Style.RESET_ALL)
        
        # right key
        if k == character:
            right_hits += 1

        # break the loop depending on time mode
        if args.use_time_mode == True:
            if end_game - game_start >= args.max_value:
                print("\nCurrent test duration " + Fore.LIGHTMAGENTA_EX + str(end_game - game_start) + Style.RESET_ALL + " exceeds maximum of " + Fore.CYAN + str(args.max_value) + Style.RESET_ALL) 
                break
        else:
            if count >= args.max_value:
                print("\nCurrent test inputs " + Fore.LIGHTGREEN_EX + str(count) + Style.RESET_ALL + " reaches maximum of " + Fore.LIGHTBLUE_EX + str(args.max_value) + Style.RESET_ALL) 
                break

    # return values
    return right_hits, count, end_game, game_start
    

def main():

    # Define argparse inputs
    parser = argparse.ArgumentParser(description='Definition of test mode')
    parser.add_argument('-utm','--use_time_mode', action='store_true', help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.', required=False)
    parser.add_argument('-mv','--max_value', type=int, help='Max number of seconds for time mode or maximum number of inputs for number of inputs mode.', required=False)

    # Parse arguments
    args = parser.parse_args()

    # check if arguments are correct
    if args.max_value == None or args.max_value <= 0:
        print("Inputted Arguments are Invalid!")
        exit(0)


    # print args
    

    # print type of the game
    if args.use_time_mode == False:
        print(f"Test running up to {args.max_value} inputs.")
    else:
        print(f"Test running up to {args.max_value} seconds.")

    # start the game
    print("To start the game press any key: ")
    start_key = readchar.readchar()

    # play the game
    right_hits, count, end_game, game_start = playGame(args)


    print(Fore.YELLOW + "Test Finished!" + Style.RESET_ALL)

    # type miss average duration
    miss_dur = sum([dur.duration for dur in INPUTS if dur.requested != dur.received])
    miss = count-right_hits

    # statistics
    statistics = {
        'accuracy': right_hits / count,
        'inputs': INPUTS,
        'number_of_hits': right_hits,
        'number_of_types': count,
        'test_duration': end_game-game_start,
        'test_end': time.ctime(end_game),
        'test_start': time.ctime(game_start),
        'type_average_duration': (sum([dur.duration for dur in INPUTS]) / len(INPUTS)) if len(INPUTS) > 0 else 0,
        'type_hit_average_duration': (sum([dur.duration for dur in INPUTS if dur.requested == dur.received]) / right_hits) if right_hits > 0 else 0,
        'type_miss_average_duration': (miss_dur / miss) if miss > 0 else 0
    }


    print()
    pprint(statistics)

if __name__ == '__main__':
    main()