#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    # Checks if n = 0, and returns 1 since factorial of 0 is 1. This makes the recursion stop.
    if n == 0:
        return 1

    # Since factorial(3) = factorial(3 - 1) * 3, The function returns the same.
    return factorial(n - 1) * n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
