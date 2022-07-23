#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    let = s.capitalize()
    teks = let[0]
    for i in range (1,len(let)):
        teks += let[i].upper() if let[i-1] == ' ' else let[i]
    return (teks)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
