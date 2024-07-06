#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Sort the array to easily find the smallest and largest sums
    arr.sort()
    
    # Calculate the minimum sum by summing the first four elements
    min_sum = sum(arr[:4])
    
    # Calculate the maximum sum by summing the last four elements
    max_sum = sum(arr[-4:])
    
    # Print the results as space-separated integers
    print(f"{min_sum} {max_sum}")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
