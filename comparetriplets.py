#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    nas = []
    x = 0
    y = 0
    for i in range(0, len(a)):

        if a[i] > b[i]:
            x = x + 1
        elif b[i] > a[i]:
            y = y + 1

    nas.append(x)
    nas.append(y)
    return nas


if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)


