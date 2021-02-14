#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    print (all([not any(ext in arr for ext in ["-*","0"]),any(s == s[::-1] for s in arr)]))