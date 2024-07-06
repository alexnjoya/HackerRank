#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Calculate the number of elements in the array
    n = len(arr)

    # Initialize counts for positive, negative, and zero elements
    pos_count = 0
    neg_count = 0
    zero_count = 0
    

    
    # Iterate over the array and count positives, negatives, and zeros
    for x in arr:
        if x > 0:
            pos_count += 1
        elif x < 0:
            neg_count += 1
        else:
            zero_count += 1
    
    # Calculate the ratios
    pos_ratio = pos_count / n
    neg_ratio = neg_count / n
    zero_ratio = zero_count / n
    
    # Print the ratios with six decimal places
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
