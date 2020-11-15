#!/usr/bin/env python
"""
With this calculator you can pick two numbers.
You will be able to multiply,divide,add & subtract.
"""

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__status__ = "Development"

Number_1 = int(input("Pick a number: "))       # Input, pick your first number
Number_2 = int(input("Pick another number: ")) # Input, it lets you pick a second number

what = input('''What would you like to do?

+ for addition
- for subtraction
* for multiplication
/ for division
''')                                   # What kind of calculation do you want to do

def main():

    if what == "+":
        print(Number_1 + Number_2)

    elif what == '-':
        print(Number_1 - Number_2)

    elif what == '*':
        print(Number_1 * Number_2)

    elif what == '*':
        print(Number_1 / Number_2)

    else:
        print('this is not a valid number')




if __name__ == '__main__':  # run tests if called from command-line
    main()
