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
    # Write your code here
    res = ''

    # if the two last positions of the string are equal to "AM"
    if s[-2:] == "AM" :
        if s[:2] == '12': #if the two first postions are equal to "12"
            res = str('00' + s[2:8]) # sum the coverted hour to the rest of the string
        else: # for cases other than 12, just remove the two last positions
            res = s[:-2]
    else:
        if s[:2] == '12': # It's PM, so simply remove the last letters
            res = s[:-2]
        else:
            res = str(int(s[:2]) + 12) + s[2:8] # to convert to 24-hours format, sum 12 plus the hours in 12-hours format
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = '07:05:45PM'

    result = timeConversion(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
