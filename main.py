#!/usr/bin/env python
# --------------------------------------------------
# Typing Test
# Filipe Gonçalves, 98083
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
from datetime import datetime

def main():

    # Define argparse inputs
    parser = argparse.ArgumentParser(description='Definition of test mode')
    parser.add_argument('-utm','--use_time_mode', action='store_true', help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.', required=False)
    parser.add_argument('-mv','--max_value', type=int, help='Max number of seconds for time mode or maximum number of inputs for number of inputs mode.', required=False)

    # Parse arguments
    args = parser.parse_args()

    if args.use_time_mode == False and args.max_value <= 0:
        print("Inputted Arguments are Invalid!")
        return

    # start the game
    print("To start the game press any key: ")
    start_key = readchar.readchar()

    statistics = {}

    print()
    pprint(statistics)

if __name__ == '__main__':
    main()