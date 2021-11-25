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
    test=s[-2:]
    new=''
    if test == 'PM':
        scratch=s[0:2]
        scratch=int(scratch)
        if scratch<12:
            scratch=scratch+12
        elif scratch==12:
            scratch=0
        if scratch < 10:
            scratch = str(scratch)
            new = '0' + scratch + s[2:8]
        else:
            scratch=str(scratch)
            new=scratch+s[2:8]
    else:
        print(s)
    return new

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()