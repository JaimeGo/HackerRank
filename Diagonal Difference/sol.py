#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    primary_sum=0
    secondary_sum=0

    n=len(arr)

    for i, row in enumerate(arr):
        primary_sum+=row[i]
        secondary_sum+=row[n-i-1]

    return abs(primary_sum-secondary_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
