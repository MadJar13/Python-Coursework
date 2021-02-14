#!/bin/python3

import math
import os
import random
import re
import sys

def getKElement(array):
    return array[k]

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key=getKElement)
    for y in range(n):    
        for x in range(m):
            print(str(arr[y][x]) + " ",end ='')
        print()