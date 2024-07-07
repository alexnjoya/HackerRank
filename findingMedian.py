#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):
 # Sort the array
 arr.sort()
 
 # Find the middle index
 mid_index = len(arr) // 2
 
 # Return the middle element (median)
 return arr[mid_index]
if __name__ == '__main__':
 fptr = open(os.environ['OUTPUT_PATH'], 'w')
 n = int(input().strip())

 arr = list(map(int, input().rstrip().split()))
 result = findMedian(arr)
 fptr.write(str(result) + '\n')
 fptr.close()