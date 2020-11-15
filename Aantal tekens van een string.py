#!/usr/bin/env python

"""
This program will display the amount of characters in a string
"""

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__status__ = "Development"



def main():
    Word = input('Type your word here: ')                        # This is your input

    print('Here are the amount of characters: ', len(Word))      # the amount of characters from a word will be printed


if __name__ == '__main__':                                       # run tests if called from command-line
    main()
