#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    
    
    sequence = []
    open_brac = ["[","{","("]
    close_brac = ["]","}",")"]
    for char in s:
        if char in open_brac:
            sequence.append(char)
        elif char in close_brac:
            if (char == "]" and sequence[-1] == "[") or (char == ")" and sequence[-1] == "(") or (char == "}" and sequence[-1] == "{"):
                sequence.pop(-1)
            elif char in close_brac and len(sequence) == 0:
                return "NO"
            else:
                return "NO"
            if len(sequence) == 0:
                return "YES"
        else:
            pass
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

