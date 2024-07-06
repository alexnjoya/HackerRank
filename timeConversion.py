#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Extract the AM/PM part from the time
    period = s[-2:]
    # Extract the hour part from the time
    hour = int(s[:2])
    
    if period == "AM":
        if hour == 12:
            # Midnight case (12 AM)
            converted_hour = "00"
        else:
            # Convert the hour to string with leading zero if needed
            converted_hour = f"{hour:02}"
    else: # period == "PM"
        if hour == 12:
            # Noon case (12 PM)
            converted_hour = "12"
        else:
            # Convert the hour to 24-hour format
            converted_hour = f"{hour + 12:02}"
    
    # Construct the new time string in 24-hour format
    converted_time = converted_hour + s[2:-2]
    
    return converted_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
