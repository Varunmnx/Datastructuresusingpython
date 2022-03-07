#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_count =0
    orange_count =0
    home = b-a
    for i in apples:
        if i+a >=s  and i+a<=t:
            apple_count +=1
    print(apple_count)
    
    for j in oranges:
        if j+b <= t and j+b >=s:
            orange_count +=1
    print(orange_count)           
        
    
    
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0]) #sams home

    t = int(first_multiple_input[1]) #sams home end

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0]) #apple tree

    b = int(second_multiple_input[1])# orange tree

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0]) # no of apples

    n = int(third_multiple_input[1]) #no of oranges

    apples = list(map(int, input().rstrip().split())) # thrown distances from apple tree

    oranges = list(map(int, input().rstrip().split()))# thrown distances from orange tree

    countApplesAndOranges(s, t, a, b, apples, oranges)
