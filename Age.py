#!/usr/bin/env python

"""
This Python script wil ask you your aga
It wil tell you in which year you're born
It will also tell you in which year you will be 50 years old
"""

import datetime


__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__status__ = "Development"

Age = int(input('How old are you?: '))  # Input that asks for your age
Year = datetime.datetime.now().year     # finds the current year based on the date of your PC/laptop
age50 = 50 - Age

def main():
    print('You were born in ', Year - Age)                  # Print year that you were born in
    print('You will be 50 in this year: ', age50 + Year)    # Print the year were you will be 50 years old


if __name__ == '__main__':                                  # run tests if called from command-line
    main()
