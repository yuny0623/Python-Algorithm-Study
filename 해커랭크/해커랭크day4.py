#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
start = True 
def superDigit(n, k):
    # Write your code here
    global start  # 전역이니까 global 선언

    if start == True: # 첫 시작이라면 
        new_str = ''
        for i in range(k): # k 번 반복 
            new_str += str(n)
            
        # print("type:",type(new_str), ",value:", new_str)
        n = int(new_str) 
        # print("type:",type(n), ",value:", n)     
        start = False 
     
    if n < 10: 
        return n
    else:
        number = 0
        number = n # 숫자로 변환
        sum_num = 0
        c = 0 
        while number > 10: 
            c = number%10 # 뒷자리부터 더해줌. 
            sum_num += c
            number = number//10 
            # print("c = ", c)
        sum_num = sum_num + number # 마지막 즉 가장큰자리수의 수를 마지막으로 더해준다. 
        return superDigit(sum_num, k)

print(superDigit(9875, 1))
