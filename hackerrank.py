#!/bin/python3

import math
import os
import random
import re
import sys

s = 'abcac'
n = 11

def repeatedString(s, n):
    # Write your code here
    s= list(s)
    counter = 0
    
    for i in s:
        if i == 'a':
            counter += 1
        print (counter)
    
    