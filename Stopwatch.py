#!/usr/bin/env python
"""
This is a stopwatch program
By pressing s on the keyboard you will stop the time
"""

import time
import sys
...

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__status__ = "Development"




def main():

    now = time.time()                 # Start counting
    time_start = time.time()
    future = now + 10
    seconds = 0
    minutes = 0

    while True:
        try:
            sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
            sys.stdout.flush()
            time.sleep(1)
            seconds = int(time.time() - time_start) - minutes * 60
            if seconds >= 60:
                minutes += 1
                seconds = 0
        except KeyboardInterrupt as s:    # If "s" is pressed, the counter will stop
            break

if __name__ == '__main__':  # run tests if called from command-line
    main()
