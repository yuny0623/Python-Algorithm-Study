'''
0536 

'''
import sys
input = sys.stdin.readline

T = int(input()) 

for _ in range(T):
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    count = 0
    li = list(input().rstrip())
    for c in li:
        if c in alpha:
            alpha.remove(c)
    for c in alpha:
        count += ord(c)
    print(count)
    
