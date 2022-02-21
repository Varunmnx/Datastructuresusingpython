#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    a=0
    n = 0
    k =0
    for i in range(len(arr)):
       if (arr[i] >0  ):
           n += 1
    #  return (n/len(arr))

       if (arr[i] < 0):
           k +=1
    #  return (k/len(arr))
       if (arr[i] == 0):
            a +=1
    print("%f" %(n/len(arr)))
    print("%f" %(k/len(arr)))
    print("%f" %(a/len(arr)))
                       

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
