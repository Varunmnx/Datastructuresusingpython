#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(ar):
    c = 0
    temp = ar[0]
    for i in range(1, len(ar)):
        if ar[i] > temp:
            temp = ar[i]
    for i in range(0, len(ar)):
        if ar[i] == temp:
            c = c + 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)

    # def brcake(arr):
    # temp = arr[0]
    # n=0
    # for i in range(1,len(arr)):
    #     if (arr[i]> temp):
    #         temp = arr[i]
    # for i in range(0,len(arr)):
    #     if(arr[i]==temp):
    #        n +=1
    # return n