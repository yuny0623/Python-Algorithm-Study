
import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    pivot = int(len(s)//2)
    
    is_palindrome = True 
    def checking(s):
        nonlocal is_palindrome                
        for i in range(len(s) // 2):      
            if s[i] != s[-1 - i]:      
                is_palindrome = False        
        return is_palindrome 
    checking(s)  # 처음 확인해보기 
    if is_palindrome == True:
        return -1 
    
    for i in range(len(s)):
        is_palindrome = True
        new_str = s[:]
        new_str = new_str[:i] + new_str[i + 1:]
        if checking(new_str) == True:
            return i 

print(palindromeIndex("baaa"))
