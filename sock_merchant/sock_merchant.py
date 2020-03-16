#!/usr/bin/env python3

import math
import os
import random
import re
import sys

# Complete the sockMercfhant function below.
def sockMerchant(n, ar):
    x = set(ar)
    for x in 
    x = { y for y in ar }

    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
