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
    # Write your code here
    n = len(arr)
    min = 0
    max = 0
    
    arr.sort()
    
    for i in range (n):
        if i != n-1:
            min += arr[i]
        if i != 0:
            max += arr[i]
            
    print('{} {}'.format(min, max))
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)