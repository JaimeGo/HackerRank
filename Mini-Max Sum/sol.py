#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_sum=0
    max_sum=0

    min_arr=arr.copy()
    max_arr=arr.copy()

    for i in range(4):
        min_num=min(min_arr)
        max_num=max(max_arr)

        min_sum+=min_num
        max_sum+=max_num

        min_arr.remove(min_num)
        max_arr.remove(max_num)

    print(str(min_sum)+" "+str(max_sum))





if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
