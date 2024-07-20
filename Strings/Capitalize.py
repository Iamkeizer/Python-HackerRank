

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l=s.split(" ")
    for i,j in zip(l,range(len(l))):
        l[j]=i.capitalize()
    return " ".join(l)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()